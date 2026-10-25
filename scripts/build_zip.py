#!/usr/bin/env python3
"""Rebuild cqu-a-zone-guide.zip from the repo source files.

Usage (from repo root):  python scripts/build_zip.py
"""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = "cqu-a-zone-guide"
OUT = ROOT / f"{NAME}.zip"

REQUIRED_FILES = [
    "SKILL.md",
    "INSTALL.md",
    "LICENSE",
    "references/campus.md",
    "references/pitfalls.md",
    "references/wellness.md",
    "references/openlib.md",
]


def validate():
    """Basic frontmatter checks mirroring quick_validate.py."""
    skill_md = ROOT / "SKILL.md"
    if not skill_md.exists():
        sys.exit("ERROR: SKILL.md not found")

    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        sys.exit("ERROR: SKILL.md has no YAML frontmatter")

    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        sys.exit("ERROR: malformed frontmatter block")
    fm = m.group(1)

    name_m = re.search(r"^name:\s*(.+)$", fm, re.MULTILINE)
    if not name_m:
        sys.exit("ERROR: missing 'name' in frontmatter")
    name = name_m.group(1).strip()
    if not re.fullmatch(r"[a-z0-9-]+", name):
        sys.exit(f"ERROR: name '{name}' is not hyphen-case")
    if name.startswith("-") or name.endswith("-") or "--" in name:
        sys.exit(f"ERROR: name '{name}' has illegal hyphen placement")
    if name != NAME:
        sys.exit(f"ERROR: name '{name}' does not match folder '{NAME}'")

    desc_m = re.search(r"^description:\s*(.+)$", fm, re.MULTILINE)
    if not desc_m:
        sys.exit("ERROR: missing 'description' in frontmatter")
    if "<" in desc_m.group(1) or ">" in desc_m.group(1):
        sys.exit("ERROR: description cannot contain angle brackets")

    if "agent_created" in fm:
        print("  ! warning: frontmatter still contains agent_created; "
              "distribution copies usually should not.")

    missing = [f for f in REQUIRED_FILES if not (ROOT / f).exists()]
    if missing:
        sys.exit(f"ERROR: missing files: {', '.join(missing)}")

    print(f"  ✓ frontmatter ok (name={name})")


def build():
    if OUT.exists():
        OUT.unlink()

    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in REQUIRED_FILES:
            src = ROOT / rel
            arcname = f"{NAME}/{rel}"  # posix separators on purpose
            z.write(src, arcname)
            print(f"  + {arcname}")

    with zipfile.ZipFile(OUT) as z:
        bad = z.testzip()
        if bad:
            sys.exit(f"ERROR: corrupt entry in zip: {bad}")

    size = OUT.stat().st_size
    print(f"\n✓ built {OUT.name}  ({len(REQUIRED_FILES)} files, {size:,} bytes)")


if __name__ == "__main__":
    print(f"Building {NAME}.zip ...")
    validate()
    build()
