# Contributing

Thank you for helping improve Awesome Operations Research. The goal is a concise, useful, well-maintained list for students, researchers, instructors, practitioners, and software developers.

This repository is released under [CC0 1.0 Universal](LICENSE).

## Contents

- [How to Suggest a Resource](#how-to-suggest-a-resource)
- [Quality Criteria](#quality-criteria)
- [Link Requirements](#link-requirements)
- [Description Style](#description-style)
- [Resource Tags](#resource-tags)
- [Formatting Rules](#formatting-rules)
- [Maintenance Scripts](#maintenance-scripts)
- [Deprecation Rules](#deprecation-rules)
- [Pull Requests](#pull-requests)
- [Broken Links](#broken-links)
- [Categories](#categories)

## How to Suggest a Resource

Open an issue or pull request with:

- Resource name.
- Official or stable URL.
- Suggested category.
- One-sentence description.
- License or commercial status when relevant.
- Suggested tags, if any.
- Whether you are affiliated with the resource.
- Why the resource belongs in this list.

## Quality Criteria

A resource should be included if it is:

- Relevant to Operations Research, optimization, simulation, analytics, decision science, or a closely related method.
- Useful to researchers, practitioners, students, educators, or software developers.
- Maintained, widely used, or historically important.
- Publicly accessible, or clearly described if commercial or access-controlled.
- Linked to an official, stable, publisher, author, institutional, or project-maintainer source.

Avoid:

- Spam or affiliate links.
- Low-quality promotional pages.
- Broken links.
- Duplicate resources.
- Unmaintained repositories unless historically important.
- Pirated book PDFs, unauthorized course mirrors, or copyright-infringing material.

## Link Requirements

- Prefer official project, publisher, society, university, DOI, arXiv, or documentation links.
- Use HTTPS where available.
- Avoid URL shorteners.
- Avoid linking to random PDF mirrors when an official page exists.
- For commercial software, link to the vendor's official product page.
- For papers, prefer DOI, publisher, arXiv, author page, or stable institutional repository.

## Description Style

Use short, factual descriptions:

```md
- [Name](https://example.com/) - Short, factual description.
```

Good:

```md
- [HiGHS](https://highs.dev/) - Open-source solver for LP, MIP, and QP models.
```

Avoid:

```md
- [Best Solver Ever](https://example.com/) - The fastest and most amazing solver on earth!!!
```

## Resource Tags

Use tags sparingly. They are meant for curated highlights, `best-of.md`, README highlights, and a few major tools or learning resources. Do not tag every entry.

Available tags:

- ⭐ Essential
- 🔥 Highly recommended
- 🎓 Academic
- 🏭 Industry
- 🆓 Free/open-source
- 💲 Commercial
- 🧪 Research-oriented
- 🧰 Practical tool
- 📚 Learning resource
- 🧑‍🏫 Teaching-friendly

Good:

```md
- ⭐ 🆓 🧰 [HiGHS](https://highs.dev/) - Open-source solver for LP, MIP, and QP models.
```

Avoid over-tagging:

```md
- ⭐ 🔥 🎓 🏭 🆓 🧪 🧰 📚 [Resource](https://example.com/) - Too many tags to be useful.
```

## Formatting Rules

- Use `- [Name](https://example.com/) - Description.` for list entries.
- Keep descriptions to one sentence when possible.
- Keep tags before the linked resource name when tags are used.
- Use "Operations Research" and "open-source" consistently.
- Put commercial software in commercial sections.
- Keep entries alphabetized where reasonable.
- Add new headings only when they will contain multiple useful resources.
- Do not add trailing whitespace or repeated blank lines.
- Keep README.md as a landing page and put long lists in topic files.

## Maintenance Scripts

Optional lightweight scripts are available in [scripts/](scripts/):

- `python3 scripts/check_internal_links.py` - Check local Markdown file links and heading anchors.
- `python3 scripts/count_resources.py` - Print approximate repository statistics.

These scripts use only the Python standard library.

## Deprecation Rules

Resources may be marked as deprecated or removed when:

- The maintainer explicitly says the project is not maintained.
- The repository has been inactive for several years and is not historically important.
- The website is unreachable and no stable replacement exists.
- The resource has been superseded by an official successor.
- The description is misleading, outdated, or promotional.

When removing a resource, include a short explanation in the pull request.

## Pull Requests

- Keep each pull request focused.
- Add resources to the most specific appropriate file.
- Update the table of contents if you add or rename headings.
- Check internal relative links before submitting.
- Explain any commercial, deprecated, or access-limited status.
- Disclose any affiliation with added resources.
- Use tags only when they improve discovery or curation.

## Broken Links

If you find a broken link:

- Open an issue with the file and line if possible.
- Suggest an official replacement link.
- If no replacement exists, suggest removing or marking the resource as deprecated.
- If a link looks malicious or unsafe, say so clearly.

## Categories

Current resource categories include:

- Start-here and curated recommendations (`README.md`, `best-of.md`).
- Knowledge maps and method guides (`maps.md`, `methodologies.md`).
- Software, solvers, and modeling tools (`softwares.md`).
- Programming libraries by language (`libraries.md`).
- Solver and modeling-language comparisons (`solver-comparison.md`, `modeling-languages.md`).
- GitHub repositories (`repositories.md`).
- Books (`books.md`).
- Courses and lectures (`courses.md`).
- Tutorials (`tutorials.md`).
- Teaching resources (`teaching.md`).
- Case studies (`case-studies.md`).
- Papers and surveys (`papers.md`).
- Research guide (`research-guide.md`).
- Journals (`journals.md`).
- Researchers (`researchers.md`).
- Universities and academic programs (`universities.md`).
- Conferences, workshops, and events (`events.md`).
- Competitions and challenges (`competitions.md`).
- Blogs, newsletters, and resource hubs (`blogs.md`).
- Communities, forums, and meetups (`meetups.md`).
- Media: podcasts, YouTube, and recorded courses (`media.md`).
- Operations Research curriculum and learning paths (`or-curriculum.md`, `learning-paths.md`).
- Datasets and benchmarks (`datasets.md`).
- Applications and industry guides (`applications.md`, `industry-guides.md`).
- Careers in Operations Research (`careers.md`).
- History of Operations Research (`history.md`).
- Operations Research and AI (`ai-and-or.md`).
