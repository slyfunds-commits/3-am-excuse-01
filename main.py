"""The 3 AM Excuse — writes the keeper line to /output/entry.txt.

Pure Python standard library only (the grader runs python:3.13-slim with no
site-packages). Deterministic: the same 111 bytes on every run, no trailing
newline.
"""

import os

KEEPER = "I read the transaction: same coin, same address, 3:14 AM. The only new thing is the hour. The hour is the scam."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)


if __name__ == "__main__":
    main()
