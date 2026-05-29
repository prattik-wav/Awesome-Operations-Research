#!/usr/bin/env python3
"""Check local Markdown file links and heading anchors.

This script intentionally uses only the Python standard library so it can run
in a fresh checkout without installing dependencies.
"""

from __future__ import annotations

import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[`*_\[\]]", "", text)
    text = re.sub(r"[^a-z0-9 -]", "", text)
    return re.sub(r"\s+", "-", text)


def anchors_for(path: pathlib.Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return {slugify(match.group(2)) for match in HEADING_RE.finditer(text)}


def main() -> int:
    markdown_files = sorted(ROOT.rglob("*.md"))
    anchor_cache: dict[pathlib.Path, set[str]] = {}
    problems: list[str] = []

    for md_file in markdown_files:
        text = md_file.read_text(encoding="utf-8")
        local_anchors = anchor_cache.setdefault(md_file, anchors_for(md_file))

        for match in LINK_RE.finditer(text):
            href = match.group(1).strip().split()[0]
            if href.startswith(("http://", "https://", "mailto:")):
                continue

            if href.startswith("#"):
                anchor = href[1:]
                if anchor not in local_anchors:
                    problems.append(f"{md_file.relative_to(ROOT)}: missing anchor {href}")
                continue

            rel, _, anchor = href.partition("#")
            if not rel:
                continue

            target = (md_file.parent / rel).resolve()
            if not target.exists():
                problems.append(f"{md_file.relative_to(ROOT)}: missing file {href}")
                continue

            if anchor and target.suffix == ".md":
                target_anchors = anchor_cache.setdefault(target, anchors_for(target))
                if anchor not in target_anchors:
                    problems.append(f"{md_file.relative_to(ROOT)}: missing anchor {href}")

    if problems:
        print("\n".join(problems))
        return 1

    print(f"OK: checked {len(markdown_files)} Markdown files for internal links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
