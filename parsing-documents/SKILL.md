---
name: parsing-documents
description: Extracts text and images from documents (PDF, Word, PowerPoint, Excel, HTML, EPUB, audio, YouTube, and more). Converts files to AI-readable Markdown using Microsoft MarkItDown with plugin extensions for math equations and PDF math/vector detection.
prerequisites: Python 3.x, LibreOffice (for legacy .doc/.ppt)
---

# Parsing Documents

This skill uses [MarkItDown](https://github.com/microsoft/markitdown) (Microsoft's Python document-to-Markdown converter) with plugin extensions for enhanced math support. It handles a wide range of formats beyond the core PDF/Word/PowerPoint.

## Core Capabilities

| Format | Support | Notes |
|--------|---------|-------|
| PDF | ✅ | Text + tables via pdfplumber, math/vector detection via PyMuPDF, OCR via plugin |
| Word (.docx) | ✅ | Text, tables, images, **math equations** (built into MarkItDown v0.1.2+) |
| PowerPoint (.pptx) | ✅ | Text, tables, charts, images, **math equations** (via markitdown-math plugin) |
| Excel (.xlsx/.xls) | ✅ | Multi-sheet tables |
| Images | ✅ | EXIF metadata + LLM captioning (via Ollama or any OpenAI-compatible API) |
| Audio | ✅ | EXIF metadata + speech transcription |
| HTML | ✅ | Full HTML-to-Markdown |
| EPUB | ✅ | E-book content extraction |
| YouTube URLs | ✅ | Video transcription |
| CSV, JSON, XML, ZIP | ✅ | Various text/archive formats |
| Legacy (.doc/.ppt) | ✅ | Requires LibreOffice (pre-conversion) |

**Math support:**
- **Word equations**: converted to LaTeX (`$...$` inline, `$$...$$` block) automatically
- **PowerPoint equations**: converted to LaTeX (via `markitdown-math` plugin)
- **PDF math**: detected via font analysis and rendered as images for vision-capable models

## Workflow

## Workflow

When tasked with parsing a document, follow these steps:

- [ ] **Step 1: Legacy Conversion (if needed)**
  - If the file is `.doc` or `.ppt`, first convert it:
    `bash scripts/convert_legacy.sh <filepath>`
  - This produces a `.docx` or `.pptx` file in the same directory.
  - Requires LibreOffice (auto-downloads portable AppImage if missing).

- [ ] **Step 2: Ensure Dependencies**
  ```bash
  pip install -r scripts/requirements.txt
  ```

- [ ] **Step 3: Convert to Markdown**
  **You do not need to choose a "script" per format.** MarkItDown auto-detects the file type (via Magika content analysis + file extension). Just run:

  ```bash
  markitdown --use-plugins <filepath> > output.md
  ```

  This works for PDF, DOCX, PPTX, XLSX, images, HTML, EPUB, audio, YouTube URLs, CSV, JSON, XML, ZIP, and more. The `markitdown-math` plugin enhances PPTX (math equations → LaTeX) and PDF (math/vector detection) automatically.

  **Variations:**
  - **Basic** (no extras): `markitdown <file> > out.md`
  - **With OCR + math**: `markitdown --use-plugins <file> > out.md`
  - **With OCR + math + LLM image captions** (vision model required):
    `markitdown --use-plugins --llm-client openai --llm-model llava <file> > out.md`

- [ ] **Step 4: Return the Markdown**
  - Read the output file and present it to the user
  - If any `{filename}_images/` directory was created, mention it to the user (images were extracted for math regions, vector graphics, or embedded images)
  - Optional: run `python scripts/test_setup.py` to verify the full setup

## LLM Vision with Ollama

Optionally use a local vision model to caption images and OCR scanned PDFs:

```bash
# 1. Install Ollama: https://ollama.com
# 2. Pull a vision model:
ollama pull llava

# 3. Verify it works:
python3 -c "
from openai import OpenAI
client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
models = client.models.list()
print('Ollama models:', [m.id for m in models])
"

# 4. Test image captioning:
markitdown --use-plugins --llm-client openai --llm-model llava some_document.pptx > output.md
```

If no `--llm-client`/`--llm-model` is provided:
- PPTX images get alt text only (no AI captioning)
- PDF OCR fallback is skipped (scanned pages return empty text)

## Notes

- **Format detection is automatic**: MarkItDown identifies the file type by content (Magika) + extension. One command for all formats.
- **PDF OCR**: Scanned PDFs need a vision model. Pass `--llm-client openai --llm-model llava --use-plugins`. The `markitdown-math` plugin includes OCR fallback for pages with no extractable text.
- **PDF math/vectors**: Rendered as PNG images in a `{filename}_images/` directory next to the output.
- **Legacy formats**: Only `.doc`/`.ppt` need manual conversion. Everything else is handled by `markitdown` directly.

## Troubleshooting

- **"No module named markitdown"**: Run `pip install 'markitdown[all]'`
- **"No plugin found"**: Run `pip install -e scripts/markitdown-math` and `pip install markitdown-ocr`
- **OCR not working**: You need a vision model. Run `ollama pull llava` and pass `--llm-client openai --llm-model llava`
- **Math not rendering**: For DOCX, use `markitdown >= 0.1.2`. For PPTX, ensure `markitdown-math` plugin is installed
- **Text gibberish in PDF**: The PDF is likely scanned. Pass a vision model for OCR
- **Images not extracted**: Images in PDFs are handled by the `markitdown-math` plugin. Ensure `--use-plugins` is passed
- **Run the test suite**: `python scripts/test_setup.py` validates the entire setup
