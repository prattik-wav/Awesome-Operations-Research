# Operations Research Research Guide

A guide for graduate students, PhD students, and early-career researchers starting or improving Operations Research research.

See also: [Papers](papers.md), [Journals](journals.md), [Events](events.md), [Datasets](datasets.md), [Universities](universities.md), [Researchers](researchers.md), and [Repositories](repositories.md).

## Contents

- [How to Start OR Research](#how-to-start-or-research)
- [Finding a Research Topic](#finding-a-research-topic)
- [Reading Papers Efficiently](#reading-papers-efficiently)
- [Literature Search Resources](#literature-search-resources)
- [Publishing in OR](#publishing-in-or)
- [Benchmarking and Computational Experiments](#benchmarking-and-computational-experiments)
- [Reproducible OR Research](#reproducible-or-research)
- [Dissertation Resources](#dissertation-resources)
- [Reviewer Checklist](#reviewer-checklist)

## How to Start OR Research

- Choose a problem class: optimization, stochastic systems, simulation, decision analysis, or an application domain.
- Read a textbook chapter before reading recent papers.
- Find one recent survey and trace its most important references.
- Reproduce a small computational result before proposing a new method.
- Talk to domain experts early if the project is application-driven.
- Keep a research log with models, assumptions, data sources, failed ideas, and experiment settings.

## Finding a Research Topic

- Look for gaps between theory and practice: models that are elegant but unrealistic, or practical problems with weak methods.
- Compare what solvers can do with what practitioners need.
- Search recent conference proceedings for open questions and benchmark trends.
- Study papers that say "future work" and verify whether the gap still exists.
- Use domain constraints as a source of novelty: uncertainty, fairness, scale, privacy, explainability, or deployment.
- Prefer questions that can be evaluated with clear baselines, data, and metrics.

## Reading Papers Efficiently

- First pass: read title, abstract, introduction, figures, computational tables, and conclusion.
- Second pass: identify the model, assumptions, theorem statements, baselines, datasets, and claimed contribution.
- Third pass: reproduce one example, proof sketch, or experiment.
- Track each paper by problem, method, data, assumptions, baselines, and limitations.
- Read with questions: What decision is being improved? What is the objective? What constraints matter? What would break in practice?

## Literature Search Resources

- [Google Scholar](https://scholar.google.com/) - Broad scholarly search and citation tracing.
- [Web of Science](https://www.webofscience.com/) - Curated citation index; institutional access often required.
- [Scopus](https://www.scopus.com/) - Abstract and citation database; institutional access often required.
- [Optimization Online](https://optimization-online.org/) - Optimization preprint repository.
- [arXiv](https://arxiv.org/) - Preprints in optimization, computer science, statistics, and applied mathematics.
- [SSRN](https://www.ssrn.com/) - Working papers in management science, economics, finance, and policy.
- [INFORMS PubsOnline](https://pubsonline.informs.org/) - INFORMS journals and magazines.
- [SIAM Publications](https://epubs.siam.org/) - SIAM journals and books.
- [ScienceDirect](https://www.sciencedirect.com/) - Elsevier journals including EJOR, Omega, and Computers & Operations Research.
- [SpringerLink](https://link.springer.com/) - Springer journals and books including Mathematical Programming and Annals of OR.

## Publishing in OR

- Use [Journals](journals.md) to choose a target venue by scope and contribution type.
- Use [Events](events.md) to find conferences and workshops for early feedback.
- Make the contribution explicit: new model, algorithm, bound, theory, computational study, software, dataset, or application insight.
- Explain assumptions and why they are acceptable for the decision context.
- Compare against credible baselines, not only weak heuristics.
- Report negative or neutral findings when they clarify where a method works.
- Write for reproducibility: data, code, solver settings, machine configuration, and random seeds should be recoverable.

## Benchmarking and Computational Experiments

- Use standard benchmarks from [Datasets](datasets.md) when available.
- Explain instance selection and whether instances were filtered.
- Report solver name, version, license class, parameters, time limits, optimality gaps, random seeds, hardware, threads, and operating system.
- Separate model-building time from solver time when relevant.
- Use multiple random seeds for stochastic algorithms.
- Include baseline methods, ablation studies, and sensitivity analyses.
- Avoid overclaiming from small or cherry-picked instance sets.
- Use [Solver Comparison](solver-comparison.md) to choose fair solver baselines.

## Reproducible OR Research

- Publish open data when licensing and privacy allow.
- Publish code with a clear README, environment file, and run instructions.
- Use notebooks for exposition but scripts for repeatable batch experiments.
- Use Docker or similar containers for complex environments.
- Pin solver versions and package versions.
- Save raw results, processed tables, and plotting scripts.
- Create GitHub releases for paper versions.
- Archive code and data with [Zenodo](https://zenodo.org/), [OSF](https://osf.io/), or institutional repositories.

## Dissertation Resources

- [Learning Paths](learning-paths.md#phd) - PhD preparation path.
- [Papers](papers.md) - Foundational and survey papers by method.
- [Journals](journals.md) - Publication venues.
- [Universities](universities.md) - Departments, programs, and research centers.
- [Researchers](researchers.md) - People and research areas to discover.
- [Competitions](competitions.md) - Benchmark-driven research opportunities.
- [Methodologies](methodologies.md) - Method-specific entry points.

## Reviewer Checklist

- [ ] Is the problem clearly motivated?
- [ ] Are assumptions stated and justified?
- [ ] Is the model reproducible from the paper?
- [ ] Are baselines included and credible?
- [ ] Are datasets available or clearly described?
- [ ] Are solver settings, random seeds, and machine details reported?
- [ ] Are optimality gaps, time limits, and failures reported honestly?
- [ ] Are sensitivity analyses included?
- [ ] Are limitations discussed?
- [ ] Is the contribution positioned against current literature?
- [ ] Can another researcher reproduce the main tables or figures?
