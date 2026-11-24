"""Everyday Wonder entry: one sentence about a small moment of wonder.

The program writes the entry sentence to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "My shadow arrived at the crossing a full step before I did, and waited for me like it knew the way home."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
