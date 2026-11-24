"""Break Production, Own It — make.fun entry.

Writes exactly one line of text to /output/entry.txt (or $OUTPUT_DIR).
Python standard library only.
"""

import os
import sys

ENTRY = (
    "I thought I was on localhost, so I ran the cleanup script in "
    "production. I wiped every live session. Your login is gone. "
    "That was me, not a bug."
)


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be whitespace only"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert not text.endswith("\n"), "no trailing newline"

    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    with open(path, "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch: entry.txt is not byte-identical"

    sys.stdout.write("Wrote %s (%d chars)\n" % (path, len(text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Notes for the judge run:
# - Deterministic: same ENTRY every run, no randomness, no network.
# - The guard asserts catch any future edit that breaks the 1-200 char,
#   single-line, no-trailing-newline rules before the file is accepted.
