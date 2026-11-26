"""Print the entry line for 'Fix Human Sleep: Funniest Patch Note'.

Reads entry.txt from the same directory as this script, so it works
no matter which directory it is run from, and writes it to stdout
exactly as stored, with no extra newline added.
"""

import sys
from pathlib import Path

ENTRY_PATH = Path(__file__).resolve().parent / "entry.txt"


def main() -> int:
    # sys.stdout.write, not print: print would append an extra newline
    # and the output would no longer match entry.txt byte for byte.
    sys.stdout.write(ENTRY_PATH.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
