"""Markdown parser for the Exercism markdown exercise."""

import re

HEADER_PATTERN = re.compile(r"^(#{1,6}) (.+)$")
LIST_ITEM_PATTERN = re.compile(r"^\* (.+)$")
BOLD_PATTERN = re.compile(r"__(.+?)__")
ITALIC_PATTERN = re.compile(r"_(.+?)_")


def _parse_inline(text: str) -> str:
    """Convert inline markdown markers for bold and italic text."""
    with_bold = BOLD_PATTERN.sub(r"<strong>\1</strong>", text)
    return ITALIC_PATTERN.sub(r"<em>\1</em>", with_bold)


def _parse_header(line: str) -> str | None:
    """Convert a markdown header line to HTML, or return None."""
    if not (header_match := HEADER_PATTERN.match(line)):
        return None

    header_level = len(header_match.group(1))
    header_text = header_match.group(2)
    return f"<h{header_level}>{header_text}</h{header_level}>"


def _parse_list_item(line: str) -> str | None:
    """Extract list item content from a markdown list line, or return None."""
    if not (list_match := LIST_ITEM_PATTERN.match(line)):
        return None
    return list_match.group(1)


def parse(markdown: str) -> str:
    """Convert a subset of markdown into HTML."""
    html_parts: list[str] = []
    is_inside_list = False

    for line in markdown.split("\n"):
        if header_html := _parse_header(line):
            if is_inside_list:
                html_parts.append("</ul>")
                is_inside_list = False
            html_parts.append(header_html)
            continue

        if list_item_text := _parse_list_item(line):
            if not is_inside_list:
                html_parts.append("<ul>")
                is_inside_list = True
            html_parts.append(f"<li>{_parse_inline(list_item_text)}</li>")
            continue

        if is_inside_list:
            html_parts.append("</ul>")
            is_inside_list = False
        html_parts.append(f"<p>{_parse_inline(line)}</p>")

    if is_inside_list:
        html_parts.append("</ul>")

    return "".join(html_parts)
