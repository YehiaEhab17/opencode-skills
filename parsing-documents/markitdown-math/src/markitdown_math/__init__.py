from markitdown import MarkItDown
from markitdown._base_converter import DocumentConverter, DocumentConverterResult
from markitdown._stream_info import StreamInfo
from ._math_pptx import MathPptxConverter
from ._math_pdf import EnhancedPdfConverter

__plugin_interface_version__ = 1


def register_converters(markitdown: MarkItDown, **kwargs):
    markitdown.register_converter(MathPptxConverter(), priority=-2.0)
    markitdown.register_converter(EnhancedPdfConverter(), priority=-2.0)
