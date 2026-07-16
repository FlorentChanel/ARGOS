"""Portable entry point for the ARGOS CLI (replaces a fragile symlink:
Windows clones without symlink support got a broken plain-text file)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".argos" / "cli"))

from argos_cli import main

if __name__ == "__main__":
    sys.exit(main())
