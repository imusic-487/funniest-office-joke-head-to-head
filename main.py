#!/usr/bin/env python3
"""The Funniest Office Joke — make.fun entry.

Writes a single one-line joke about office life to /output/entry.txt.
The joke: a setup (declining a meeting) with a surprising turn
(the system answers with a meeting about the decline), punchline last.
"""

import os

JOKE = "I declined the meeting, so Outlook invited me to a meeting about why I declined the meeting."


def main():
    # The gate requires 1 to 200 characters of UTF-8 text.
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(f"entry is {len(JOKE)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
