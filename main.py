#!/usr/bin/env python3
"""Print the one-line entry for the 'How Many Tabs Do You Have Open?' bounty."""

import pathlib


def load_line() -> str:
    path = pathlib.Path(__file__).with_name("entry.txt")
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("entry.txt is empty")
    return text


def main() -> None:
    line = load_line()
    print(line)


if __name__ == "__main__":
    main()
