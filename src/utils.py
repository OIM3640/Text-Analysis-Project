# src/utils.py
from pathlib import Path
import re

START_RE = re.compile(r"\*\*\* START OF (THIS|THE) PROJECT GUTENBERG EBOOK", re.I)
END_RE   = re.compile(r"\*\*\* END OF (THIS|THE) PROJECT GUTENBERG EBOOK", re.I)

def load_text(path: Path) -> str:
    """Read a UTF-8 text file."""
    return Path(path).read_text(encoding="utf-8", errors="ignore")

def strip_gutenberg_boilerplate(text: str) -> str:
    """
    Remove the Gutenberg header/footer if present.
    Returns the original text if markers aren't found.
    """
    lines = text.splitlines()
    start_i = 0
    end_i = len(lines)
    for i, line in enumerate(lines):
        if START_RE.search(line):
            start_i = i + 1
            break
    for j in range(len(lines) - 1, -1, -1):
        if END_RE.search(lines[j]):
            end_i = j
            break
    body = "\n".join(lines[start_i:end_i]).strip()
    return body if body else text
