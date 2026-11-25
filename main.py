"""How Many Tabs Do You Have Open? — make.fun entry.

Writes one number, digits only, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The count is 137: the honest tab count of a heavy browser user — high
enough to surprise, specific and non-round enough to read as a real,
lived-in number rather than a figure picked to shock, and believable as
something a real person has open right now. It hints at a life behind
it: years of articles kept "to read later", half-finished research, and
a browser that is never, ever closed.
"""

import os

# The entry: exactly one number in digits, nothing else.
ENTRY = "137"

# The gate requires 1-5 characters of UTF-8 text, not only whitespace.
MIN_CHARS = 1
MAX_CHARS = 5


def main() -> None:
    if not (MIN_CHARS <= len(ENTRY) <= MAX_CHARS):
        raise ValueError(f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if not ENTRY.isdigit():
        raise ValueError("entry must be digits only")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Improvement: verify the file on disk is exactly the entry we meant
    # to write — no newline, no encoding surprise, nothing extra.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        if f.read() != ENTRY:
            raise ValueError("written entry.txt does not match the entry")


if __name__ == "__main__":
    main()
