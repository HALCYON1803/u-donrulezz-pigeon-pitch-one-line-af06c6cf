#!/usr/bin/env python3
"""Pigeon Pitch, One Line.

Writes the pigeon's one-line elevator pitch to /output/entry.txt.
"""

import os

ENTRY = (
    "My startup has 40,000 daily active users perched on every statue downtown, "
    "zero churn, and I'm raising a seed round \u2014 literally, birdseed "
    "\u2014 at a CAC of one crumb."
)

# The gate requires 1-200 characters; fail loudly rather than submit junk.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
