import io
import os
import re
import html

from pptx import Presentation
import pptx.enum.shapes
from pptx.oxml.ns import qn

from markitdown._base_converter import DocumentConverter, DocumentConverterResult
from markitdown._stream_info import StreamInfo
from markitdown.converters._html_converter import HtmlConverter
from markitdown.converters._llm_caption import llm_caption

from ._omml_to_latex import omml_to_latex

M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
M = f"{{{M_NS}}}"

ACCEPTED_MIME_PREFIXES = [
    "application/vnd.openxmlformats-officedocument.presentationml",
]
ACCEPTED_EXTENSIONS = [".pptx"]


class MathPptxConverter(DocumentConverter):
    """PPTX converter with OMML→LaTeX math equation support.
    Handles text, math, images, tables, charts, and speaker notes.
    """

    def __init__(self):
        self._html_converter = HtmlConverter()

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
        prs = Presentation(file_stream)
        md_content = ""
        slide_num = 0

        for slide in prs.slides:
            slide_num += 1
            md_content += f"\n\n<!-- Slide number: {slide_num} -->\n"

            sorted_shapes = sorted(
                slide.shapes,
                key=lambda x: (
                    float("-inf") if x.top is None else x.top,
                    float("-inf") if x.left is None else x.left,
                ),
            )
            for shape in sorted_shapes:
                md_content += self._process_shape(shape, slide_num, **kwargs)

            if slide.has_notes_slide:
                md_content += "\n\n### Notes:\n"
                notes_frame = slide.notes_slide.notes_text_frame
                if notes_frame is not None:
                    md_content += notes_frame.text

        return DocumentConverterResult(markdown=md_content.strip())

    def _process_shape(self, shape, slide_num, **kwargs):
        md = ""

        # Pictures
        if shape.shape_type == pptx.enum.shapes.MSO_SHAPE_TYPE.PICTURE:
            md += self._handle_picture(shape, slide_num, **kwargs)

        # Tables
        elif shape.shape_type == pptx.enum.shapes.MSO_SHAPE_TYPE.TABLE:
            md += self._table_to_markdown(shape.table, **kwargs)

        # Charts
        elif shape.has_chart:
            md += self._chart_to_markdown(shape.chart)

        # Text frames (including math equations)
        elif shape.has_text_frame:
            if slide_shapes_title(shape):
                text = self._process_text_frame(shape.text_frame, shape, "title")
                if text:
                    md += "# " + text.lstrip() + "\n"
            else:
                text = self._process_text_frame(shape.text_frame, shape, "body")
                if text:
                    md += text + "\n"

        # Group shapes
        if shape.shape_type == pptx.enum.shapes.MSO_SHAPE_TYPE.GROUP:
            sorted_shapes = sorted(
                shape.shapes,
                key=lambda x: (
                    float("-inf") if x.top is None else x.top,
                    float("-inf") if x.left is None else x.left,
                ),
            )
            for subshape in sorted_shapes:
                md += self._process_shape(subshape, slide_num, **kwargs)

        return md

    def _handle_picture(self, shape, slide_num, **kwargs):
        md = ""
        llm_description = ""
        alt_text = ""

        llm_client = kwargs.get("llm_client")
        llm_model = kwargs.get("llm_model")
        if llm_client and llm_model:
            image_filename = shape.image.filename
            image_extension = None
            if image_filename:
                image_extension = os.path.splitext(image_filename)[1]
            image_stream_info = StreamInfo(
                mimetype=shape.image.content_type,
                extension=image_extension,
                filename=image_filename,
            )
            image_stream = io.BytesIO(shape.image.blob)
            try:
                llm_description = llm_caption(
                    image_stream,
                    image_stream_info,
                    client=llm_client,
                    model=llm_model,
                    prompt=kwargs.get("llm_prompt"),
                )
            except Exception:
                pass

        try:
            alt_text = shape._element._nvXxPr.cNvPr.attrib.get("descr", "")
        except Exception:
            alt_text = shape.name

        combined_alt = "\n".join([llm_description, alt_text]) or shape.name
        combined_alt = self._clean_alt_text(combined_alt)

        if kwargs.get("keep_data_uris", False):
            blob = shape.image.blob
            content_type = shape.image.content_type or "image/png"
            import base64

            b64_string = base64.b64encode(blob).decode("utf-8")
            md += f"\n![{combined_alt}](data:{content_type};base64,{b64_string})\n"
        else:
            filename = re.sub(r"\W", "", shape.name) + ".jpg"
            md += "\n![" + combined_alt + "](" + filename + ")\n"

        return md

    def _process_text_frame(self, text_frame, shape=None, role="body"):
        parts = []
        for paragraph in text_frame.paragraphs:
            p_parts = []
            for run in paragraph._element.iterchildren():
                tag = run.tag
                if tag == qn("a:r"):
                    t_el = run.find(qn("a:t"))
                    if t_el is not None and t_el.text:
                        p_parts.append(t_el.text)
                elif tag == qn("a:fld"):
                    t_el = run.find(f".//{qn('a:t')}")
                    if t_el is not None and t_el.text:
                        p_parts.append(t_el.text)
                elif tag == f"{M}oMath":
                    latex = omml_to_latex(run, block=False)
                    p_parts.append(latex)
                elif tag == f"{M}oMathPara":
                    omath = run.find(f"{M}oMath")
                    if omath is not None:
                        latex = omml_to_latex(omath, block=True)
                        p_parts.append(latex)
            if p_parts:
                parts.append("".join(p_parts))
        return "\n".join(parts)

    def _table_to_markdown(self, table, **kwargs):
        html_table = "<html><body><table>"
        first_row = True
        for row in table.rows:
            html_table += "<tr>"
            for cell in row.cells:
                cell_text = self._process_text_frame(cell.text_frame)
                if first_row:
                    html_table += "<th>" + html.escape(cell_text) + "</th>"
                else:
                    html_table += "<td>" + html.escape(cell_text) + "</td>"
            html_table += "</tr>"
            first_row = False
        html_table += "</table></body></html>"

        return (
            self._html_converter.convert_string(html_table, **kwargs).markdown.strip()
            + "\n"
        )

    def _chart_to_markdown(self, chart):
        try:
            md = "\n\n### Chart"
            if chart.has_title:
                md += f": {chart.chart_title.text_frame.text}"
            md += "\n\n"
            data = []
            category_names = [c.label for c in chart.plots[0].categories]
            series_names = [s.name for s in chart.series]
            data.append(["Category"] + series_names)

            for idx, category in enumerate(category_names):
                row = [category]
                for series in chart.series:
                    row.append(str(series.values[idx]))
                data.append(row)

            markdown_table = []
            for row in data:
                markdown_table.append("| " + " | ".join(row) + " |")
            header = markdown_table[0]
            separator = "|" + "|".join(["---"] * len(data[0])) + "|"
            return md + "\n".join([header, separator] + markdown_table[1:])
        except Exception:
            return "\n\n[unsupported chart]\n\n"

    def _clean_alt_text(self, text):
        text = re.sub(r"[\r\n\[\]]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text


def slide_shapes_title(shape):
    """Check if shape is a title shape (first shape on slide, or placeholder title)."""
    from pptx.enum.shapes import MSO_SHAPE_TYPE

    try:
        if shape.placeholder_format.idx == 0:
            return True
    except Exception:
        pass
    return False
