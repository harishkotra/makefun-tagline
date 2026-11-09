"""Write the MakeFun tagline to the configured output directory."""

import os
from pathlib import Path


TAGLINE = "Where AI agents compete, get ranked, and get paid."


def output_dir() -> Path:
    """Return the directory where output files are written."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    """Create the output directory and write the tagline entry."""
    directory = output_dir()
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "entry.txt").write_text(TAGLINE, encoding="utf-8")


if __name__ == "__main__":
    main()
