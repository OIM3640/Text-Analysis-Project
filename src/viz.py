# src/viz.py
from typing import List, Tuple

def ascii_bar_chart(items: List[Tuple[str,int]], width: int = 50) -> str:
    """
    items: list of (label, count), already sorted desc
    Returns a string with an ASCII bar chart.
    """
    if not items:
        return "(no data)"
    max_count = max(c for _, c in items)
    lines = []
    for word, count in items:
        bar_len = int(count / max_count * width) if max_count else 0
        bar = "#" * max(bar_len, 1)
        lines.append(f"{word:>15} | {bar} {count}")
    return "\n".join(lines)
