"""Entry for make.fun bounty: The Meeting That Should Have Been an Email.

Writes one single-line joke about a meeting that should have been an
email to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Writes ONLY to the output directory, never to the repository directory:
in the grader the repository is read-only.
"""

import os
import sys

ENTRY = (
    "Ninety minutes, twelve people, zero decisions — and the one thing "
    "we agreed on: the email we never sent was the only one who did its job."
)


def main() -> int:
    # Grader runs with the repo read-only: resolve the output directory from
    # the environment first, never write next to the source files.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Single line, no trailing newline (a newline would count as a char).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
