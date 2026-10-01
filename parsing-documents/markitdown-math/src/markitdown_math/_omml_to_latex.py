from xml.etree.ElementTree import Element

from docxlatex.parser.ommlparser import OMMLParser

_PARSER = OMMLParser()


def omml_to_latex(element: Element, block: bool = False) -> str:
    latex = _PARSER.parse(element)
    if block:
        return f"$$ {latex} $$"
    return f"$ {latex} $"
