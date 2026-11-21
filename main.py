#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

Deterministic: the same bytes on every run. No network, no input.
"""

import os

TEXT = (
    "The stone in his coat pocket had been there all winter, "
    "worn smooth by his thumb. It was warm now, not from any fire, "
    "just from being carried. He set it on the windowsill beside "
    "the late light and left it there, and the light stayed with "
    "it a while longer."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
