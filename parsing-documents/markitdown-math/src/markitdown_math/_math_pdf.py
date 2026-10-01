import io
import os
import hashlib
import re

import fitz
import pdfplumber
import pdfminer.high_level

from markitdown._base_converter import DocumentConverter, DocumentConverterResult
from markitdown._stream_info import StreamInfo
from markitdown.converters._llm_caption import llm_caption

MATH_FONTS = [
    "cambria math",
    "mathematica",
    "math",
    "symbol",
    "mt",
    "eufm",
    "cmr",
    "cmmi",
    "cmsy",
    "msam",
    "msbm",
    "stix",
    "xits",
    "asana math",
    "latin modern math",
    "tex gyre",
]

MATH_UNICODE_RANGES = [
    (0x2200, 0x22FF),
    (0x2A00, 0x2AFF),
    (0x1D400, 0x1D7FF),
    (0x2100, 0x214F),
    (0x2190, 0x21FF),
    (0x27C0, 0x27EF),
    (0x2900, 0x297F),
    (0x2030, 0x205E),
]

ACCEPTED_MIME_PREFIXES = ["application/pdf", "application/x-pdf"]
ACCEPTED_EXTENSIONS = [".pdf"]

# Pattern for MasterFormat-style partial numbering (e.g., ".1", ".2")
PARTIAL_NUMBERING_PATTERN = re.compile(r"^\.\d+$")


class EnhancedPdfConverter(DocumentConverter):
    """PDF converter combining pdfplumber text/table extraction
    with PyMuPDF math detection and vector graphic rendering.
    """

    def accepts(self, file_stream, stream_info, **kwargs):
        mimetype = (stream_info.mimetype or "").lower()
        extension = (stream_info.extension or "").lower()
        if extension in ACCEPTED_EXTENSIONS:
            return True
        for prefix in ACCEPTED_MIME_PREFIXES:
            if mimetype.startswith(prefix):
                return True
        return False

    def convert(self, file_stream, stream_info, **kwargs):
        pdf_bytes = io.BytesIO(file_stream.read())

        markdown = self._extract_text(pdf_bytes, **kwargs)
        math_images_md = self._extract_math_and_vectors(pdf_bytes, stream_info)

        result = markdown
        if math_images_md:
            result += "\n\n" + math_images_md

        return DocumentConverterResult(markdown=result)

    def _extract_text(self, pdf_bytes, **kwargs):
        def merge_partial_numbering(text: str) -> str:
            lines = text.split("\n")
            result = []
            i = 0
            while i < len(lines):
                line = lines[i]
                stripped = line.strip()
                if PARTIAL_NUMBERING_PATTERN.match(stripped):
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines):
                        result.append(f"{stripped} {lines[j].strip()}")
                        i = j + 1
                        continue
                result.append(line)
                i += 1
            return "\n".join(result)

        chunks = []
        llm_client = kwargs.get("llm_client")
        llm_model = kwargs.get("llm_model")

        try:
            with pdfplumber.open(pdf_bytes) as pdf:
                for page_num, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text and text.strip():
                        chunks.append(text.strip())
                    elif llm_client and llm_model:
                        ocr_text = self._ocr_page(pdf_bytes, page_num, **kwargs)
                        if ocr_text:
                            chunks.append(f"[OCR]: {ocr_text}")
                    page.close()
            if chunks:
                return merge_partial_numbering("\n\n".join(chunks))
        except Exception:
            pass

        pdf_bytes.seek(0)
        text = pdfminer.high_level.extract_text(pdf_bytes)
        if text.strip():
            return merge_partial_numbering(text)

        if llm_client and llm_model:
            return self._ocr_full_document(pdf_bytes, **kwargs)

        return ""

    def _ocr_page(self, pdf_bytes, page_num, **kwargs):
        try:
            doc = fitz.open(stream=pdf_bytes, filetype="pdf")
            page = doc.load_page(page_num)
            pix = page.get_pixmap(dpi=300)
            img_bytes = pix.tobytes("png")
            doc.close()

            page_stream = io.BytesIO(img_bytes)
            page_info = StreamInfo(mimetype="image/png")
            ocr_prompt = (
                kwargs.get("llm_prompt")
                or "Extract all text from this document page. Return only the text content, preserving structure."
            )
            return llm_caption(
                page_stream,
                page_info,
                client=kwargs["llm_client"],
                model=kwargs["llm_model"],
                prompt=ocr_prompt,
            )
        except Exception:
            return ""

    def _ocr_full_document(self, pdf_bytes, **kwargs):
        try:
            doc = fitz.open(stream=pdf_bytes, filetype="pdf")
            texts = []
            for page_num in range(len(doc)):
                text = self._ocr_page(pdf_bytes, page_num, **kwargs)
                if text:
                    texts.append(f"--- Page {page_num + 1} ---\n{text}")
            doc.close()
            return "\n\n".join(texts) if texts else ""
        except Exception:
            return ""

    def _extract_math_and_vectors(self, pdf_bytes, stream_info):
        """Detect math regions and vector graphics, render as images."""
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        base_name = stream_info.filename or "document"
        if base_name:
            base_name = os.path.splitext(base_name)[0]
        base_name = re.sub(r"[^A-Za-z0-9_]", "_", base_name)

        dir_name = "."
        if stream_info.local_path:
            dir_name = os.path.dirname(stream_info.local_path)

        img_dir = os.path.join(dir_name, f"{base_name}_images")
        os.makedirs(img_dir, exist_ok=True)

        md_chunks = []
        img_hashes = {}
        all_paths = []

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE).get(
                "blocks", []
            )

            text_blocks = [b for b in blocks if b["type"] == 0]
            image_blocks = [b for b in blocks if b["type"] == 1]

            # Math detection
            for block in text_blocks:
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        font = span.get("font", "").lower()
                        text = span.get("text", "")
                        if not text.strip():
                            continue
                        is_math = any(mf in font for mf in MATH_FONTS)
                        if not is_math:
                            for ch in text:
                                cp = ord(ch)
                                for lo, hi in MATH_UNICODE_RANGES:
                                    if lo <= cp <= hi:
                                        is_math = True
                                        break
                        if is_math:
                            path = self._render_span(
                                page, span, img_dir, img_hashes, page_num + 1
                            )
                            if path:
                                all_paths.append(path)
                                md_chunks.append(f"![]({path})")

            # Vector graphics
            drawings = page.get_drawings()
            covered = []
            for b in text_blocks:
                covered.append(fitz.Rect(b["bbox"]))
            for b in image_blocks:
                covered.append(fitz.Rect(b["bbox"]))

            regions = []
            for d in drawings:
                rect = d.get("rect")
                if rect is None:
                    continue
                r = fitz.Rect(rect)
                if r.width < 20 or r.height < 20:
                    continue
                if not any(r.intersects(c) for c in covered):
                    regions.append(r)

            merged = self._merge_rects(regions)
            for region in merged:
                path = self._render_rect(
                    page, region, img_dir, img_hashes, page_num + 1
                )
                if path:
                    all_paths.append(path)
                    md_chunks.append(f"![]({path})")

            # Embedded images
            for img_index, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                base_image = doc.extract_image(xref)
                img_bytes = base_image["image"]
                img_ext = base_image["ext"]
                h = hashlib.md5(img_bytes).hexdigest()
                if h in img_hashes:
                    path = img_hashes[h]
                else:
                    name = f"page_{page_num + 1}_img_{len(img_hashes) + 1}.{img_ext}"
                    img_hashes[h] = name
                    path = os.path.join(img_dir, name)
                    with open(path, "wb") as f:
                        f.write(base_image["image"])
                rel_path = os.path.join(img_dir, os.path.basename(path))
                md_chunks.append(f"![]({rel_path})")

        if not md_chunks:
            import shutil

            try:
                shutil.rmtree(img_dir)
            except Exception:
                pass
            return ""

        return "\n\n".join(md_chunks)

    def _render_span(self, page, span, img_dir, img_hashes, page_num):
        rect = fitz.Rect(span["bbox"])
        return self._render_rect(page, rect, img_dir, img_hashes, page_num)

    def _render_rect(self, page, rect, img_dir, img_hashes, page_num):
        pix = page.get_pixmap(clip=rect, dpi=200)
        img_bytes = pix.tobytes("png")
        h = hashlib.md5(img_bytes).hexdigest()
        if h in img_hashes:
            return img_hashes[h]

        name = f"page_{page_num}_region_{len(img_hashes) + 1}.png"
        img_hashes[h] = name
        path = os.path.join(img_dir, name)
        pix.save(path)
        return path

    def _merge_rects(self, rects):
        if not rects:
            return []
        merged = []
        for r in sorted(rects, key=lambda x: (x.y0, x.x0)):
            if merged and r.intersects(merged[-1]):
                merged[-1] = merged[-1].include_rect(r)
            else:
                merged.append(r)
        return merged
