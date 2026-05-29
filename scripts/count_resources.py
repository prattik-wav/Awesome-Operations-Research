#!/usr/bin/env python3
"""Print approximate resource statistics for the awesome list."""

from __future__ import annotations

import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def linked_bullets(path: str) -> int:
    return len(re.findall(r"^- .*\[[^\]]+\]\(", read(path), flags=re.MULTILINE))


def table_resource_rows(path: str) -> int:
    rows = 0
    for line in read(path).splitlines():
        if line.startswith("|") and "](" in line and "---" not in line:
            rows += 1
    return rows


def main() -> None:
    markdown_files = sorted(path for path in ROOT.glob("*.md"))
    non_topic = {
        "CHANGELOG.md",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        "README.md",
        "ROADMAP.md",
        "SECURITY.md",
    }
    topic_guides = sum(1 for path in markdown_files if path.name not in non_topic)
    categories = 0
    resources = 0

    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        categories += len(re.findall(r"^## (?!Contents$).+", text, flags=re.MULTILINE))
        rel = path.name
        resources += linked_bullets(rel) + table_resource_rows(rel)

    stats = {
        "markdown_files": len(markdown_files),
        "topic_guides": topic_guides,
        "major_categories_and_subsections": categories,
        "curated_resources_and_cross_links": resources,
        "software_solver_entries": linked_bullets("softwares.md"),
        "libraries": linked_bullets("libraries.md"),
        "books": linked_bullets("books.md"),
        "courses": linked_bullets("courses.md"),
        "papers": linked_bullets("papers.md"),
        "journals": table_resource_rows("journals.md"),
        "researchers": linked_bullets("researchers.md"),
        "universities_programs_centers": table_resource_rows("universities.md") + linked_bullets("universities.md"),
        "datasets_benchmarks": linked_bullets("datasets.md"),
        "career_roles": 14,
        "industry_guides": 13,
    }

    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
