# Teaching Operations Research

Resources and course-design ideas for instructors teaching Operations Research, optimization, simulation, analytics, and prescriptive modeling.

See also: [Courses](courses.md), [Books](books.md), [Datasets](datasets.md), [Case Studies](case-studies.md), [Tutorials](tutorials.md), [Software](softwares.md), and [Best Of](best-of.md).

## Contents

- [Course Design](#course-design)
- [Introductory OR Course](#introductory-or-course)
- [Optimization Course](#optimization-course)
- [Simulation Course](#simulation-course)
- [Supply Chain OR Course](#supply-chain-or-course)
- [Analytics and Prescriptive Modeling Course](#analytics-and-prescriptive-modeling-course)
- [Classroom Software](#classroom-software)
- [Teaching Datasets](#teaching-datasets)
- [Case Studies](#case-studies)
- [Assignment Ideas](#assignment-ideas)
- [Project Ideas](#project-ideas)
- [Assessment Ideas](#assessment-ideas)
- [Open Educational Resources](#open-educational-resources)

## Course Design

- Start with decisions, not algorithms: define decision variables, objectives, constraints, uncertainty, and stakeholders.
- Use one small model repeatedly to teach formulation, sensitivity, duality, implementation, and communication.
- Pair exact methods with simulation or heuristics so students learn when models are approximations.
- Require short model memos, not only code or numeric answers.
- Include solver-log literacy: infeasibility, unboundedness, gaps, presolve, time limits, and numerical warnings.

## Introductory OR Course

- Core topics: modeling, LP, duality, sensitivity, transportation, assignment, network models, integer programming, queueing, inventory, simulation, and decision analysis.
- Suggested books: [Introduction to Operations Research](books.md#general-operations-research), [Operations Research: An Introduction](books.md#general-operations-research), and [Applied Mathematical Programming](books.md#modeling-and-mathematical-programming).
- Suggested software: Excel Solver, OpenSolver, PuLP, Pyomo, OR-Tools, and visualization tools.
- Suggested projects: product mix, blending, transportation, facility location, staffing, queueing simulation, and inventory policy simulation.

## Optimization Course

- Core topics: LP, duality, simplex, interior-point methods, integer programming, branch-and-bound, cuts, nonlinear optimization, convexity, and decomposition.
- Suggested books: [Introduction to Linear Optimization](books.md#linear-and-integer-programming), [Integer Programming](books.md#linear-and-integer-programming), and [Convex Optimization](books.md#nonlinear-and-convex-optimization).
- Suggested software: Pyomo, JuMP, AMPL, GAMS, HiGHS, SCIP, Gurobi, CPLEX, and MOSEK.
- Suggested projects: MIP formulation challenge, solver comparison, decomposition prototype, and benchmark replication.

## Simulation Course

- Core topics: discrete-event simulation, random variates, input modeling, output analysis, warm-up, replications, variance reduction, validation, and simulation optimization.
- Suggested books: [Simulation Modeling and Analysis](books.md#simulation) and [Discrete-Event System Simulation](books.md#simulation).
- Suggested software: SimPy, simmer, Arena, Simio, AnyLogic, JaamSim, and Python/R statistics tools.
- Suggested projects: call center, emergency department, warehouse, production line, airport security, or public service simulation.

## Supply Chain OR Course

- Core topics: demand forecasting, inventory, network design, facility location, transportation, routing, production planning, uncertainty, and resilience.
- Suggested books: [Supply Chain Management](books.md#inventory-and-supply-chain), [Designing and Managing the Supply Chain](books.md#inventory-and-supply-chain), and [Foundations of Inventory Management](books.md#inventory-and-supply-chain).
- Suggested software: Pyomo, JuMP, Gurobi, CPLEX, OR-Tools, AnyLogic, SimPy, and spreadsheet models.
- Suggested projects: network design, multi-period planning, safety stock simulation, and vehicle routing.

## Analytics and Prescriptive Modeling Course

- Core topics: prediction-to-optimization pipelines, decision-focused evaluation, experiments, dashboards, simulation, and scenario analysis.
- Suggested resources: [MIT Analytics Edge](courses.md#data-science-analytics-and-or), [AI and OR](ai-and-or.md), and [Decision Intelligence](ai-and-or.md#decision-intelligence).
- Suggested software: Python, SQL, scikit-learn, CVXPY, OR-Tools, Pyomo, BI tools, and notebooks.
- Suggested projects: forecast demand and optimize inventory, predict delays and optimize schedules, or build a decision-support dashboard.

## Classroom Software

- [Excel Solver](softwares.md#spreadsheet-and-teaching-tools) - Familiar spreadsheet tool for first optimization models.
- [OpenSolver](softwares.md#spreadsheet-and-teaching-tools) - Free spreadsheet optimization add-in.
- [SolverStudio](softwares.md#spreadsheet-and-teaching-tools) - Spreadsheet interface to modeling languages.
- [LINDO/LINGO](softwares.md#spreadsheet-and-teaching-tools) - Teaching-friendly commercial modeling system.
- [AMPL](modeling-languages.md#language-notes) - Clean algebraic modeling language for optimization courses.
- [Pyomo](libraries.md#python) - Python algebraic modeling package.
- [PuLP](libraries.md#python) - Lightweight Python LP/MIP modeling package.
- [OR-Tools](softwares.md#open-source-solvers) - Practical toolkit for routing, scheduling, flows, and CP-SAT.
- [JuMP](libraries.md#julia) - Julia optimization modeling language.
- [SimPy](libraries.md#python) - Python discrete-event simulation.
- [Arena](softwares.md#simulation-software) - Commercial discrete-event simulation software.
- [Simio](softwares.md#simulation-software) - Commercial simulation and scheduling platform.
- [AnyLogic](softwares.md#simulation-software) - Commercial multi-method simulation platform.

## Teaching Datasets

- [Netlib LP](datasets.md#optimization-benchmarks) - Classic LP benchmark examples.
- [MIPLIB](datasets.md#optimization-benchmarks) - MIP benchmark instances for advanced students.
- [OR-Library](datasets.md#optimization-benchmarks) - Broad collection of teaching-friendly OR instances.
- [CVRPLIB](datasets.md#transportation-and-routing-datasets) - Vehicle routing instances.
- [PSPLIB](datasets.md#scheduling-benchmarks) - Project scheduling instances.
- [Call Center Data](datasets.md#simulation-and-queueing-datasets) - Service-system data for queueing and simulation.
- [OpenStreetMap](datasets.md#transportation-and-routing-datasets) - Geographic data for routing and location projects.

## Case Studies

- Use [Case Studies](case-studies.md) for applied examples in airlines, UPS-style routing, Amazon-style fulfillment, healthcare, sports scheduling, energy, disaster response, and public-sector allocation.
- Pair each case with one formulation exercise and one communication exercise.
- Ask students to identify assumptions, stakeholders, objective functions, and possible unintended consequences.

## Assignment Ideas

- Product mix LP - Teach decision variables, objective functions, resource constraints, and sensitivity.
- Blending problem - Teach formulation, proportions, quality constraints, and dual values.
- Transportation problem - Teach network structure, flows, and costs.
- Assignment problem - Teach binary variables and matching.
- Facility location - Teach fixed costs, service regions, and tradeoffs.
- Vehicle routing - Teach combinatorial complexity and heuristics.
- Inventory policy simulation - Teach uncertainty and service levels.
- Queueing simulation - Teach congestion, utilization, and waiting.
- Workforce scheduling - Teach coverage constraints and fairness.
- Hospital capacity planning - Teach simulation, uncertainty, and stakeholder communication.

## Project Ideas

- Build a complete decision-support notebook for a local nonprofit or campus service.
- Compare two solvers on a benchmark set and write a reproducibility report.
- Design a supply chain network under demand growth scenarios.
- Build a simulation model and validate it against observed data.
- Create an interactive dashboard around an optimization model.
- Reproduce a small published computational experiment.

## Assessment Ideas

- Model formulation exams with short written justifications.
- Code assignments with solver logs and validation questions.
- Case memos for nontechnical stakeholders.
- Oral presentations explaining assumptions and recommendations.
- Reproducibility reports with data, code, environment, and results.
- Peer review of model assumptions and communication.

## Open Educational Resources

- [MIT OpenCourseWare OR courses](courses.md#introductory-operations-research) - Free course materials.
- [Stanford EE364a](courses.md#convex-optimization) - Free convex optimization materials.
- [Applied Mathematical Programming](books.md#modeling-and-mathematical-programming) - Free MIT-hosted text.
- [Convex Optimization](books.md#nonlinear-and-convex-optimization) - Free textbook by Boyd and Vandenberghe.
- [ND Pyomo Cookbook](tutorials.md#python-tutorials) - Open Pyomo teaching notebooks.
- [OR-Tools Guides](tutorials.md#python-tutorials) - Free tutorials and examples.
