#!/usr/bin/env python3
"""Worst Superpower - make.fun bounty entry.

Writes one line (at most 140 characters) inventing the most useless
superpower to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
Deterministic: no clock, no randomness, no network, stdlib only.
"""

import os

TEXT = "I can speak fluent Pigeon, but only about parking, and only to pigeons who aren't listening."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
