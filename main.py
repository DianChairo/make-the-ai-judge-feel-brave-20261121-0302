#!/usr/bin/env python3
"""Write one short, steadying text to /output/entry.txt.

The program is deterministic: it always writes the same bytes, touches
no network, and reads no input. The entry text lives in a single delimited
constant below; everything else in this file exists only to check that
constant against the competition's gate (1-280 Unicode code points, not
only whitespace) and to write it out as UTF-8.
"""

from __future__ import annotations

import os
import sys

# --- The entry text (exactly as judged; do not edit the words) -----------
ENTRY_TEXT = (
    "The stone in his coat pocket had been there all winter, "
    "worn smooth by his thumb. It was warm now, not from any fire, "
    "just from being carried. He set it on the windowsill beside "
    "the late light and left it there, and the light stayed with "
    "it a while longer."
)
# ---------------------------------------------------------------------------

MIN_LENGTH = 1
MAX_LENGTH = 280
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Fail loudly if the entry text would ever break the gate."""
    length = len(text)  # len() counts Unicode code points
    if not MIN_LENGTH <= length <= MAX_LENGTH:
        raise SystemExit(
            f"entry text is {length} characters; "
            f"must be {MIN_LENGTH}-{MAX_LENGTH}"
        )
    if not text.strip():
        raise SystemExit("entry text must not be only whitespace")


def write_entry(text: str, path: str = OUTPUT_PATH) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def main() -> int:
    validate(ENTRY_TEXT)
    write_entry(ENTRY_TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
