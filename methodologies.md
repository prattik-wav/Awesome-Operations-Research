# Operations Research by Methodology

Use this guide when you know the method you want to learn or apply. It points to the most useful entry points across the repository without duplicating the full resource lists.

See also: [Books](books.md), [Courses](courses.md), [Papers](papers.md), [Software](softwares.md), [Datasets](datasets.md), [Researchers](researchers.md), and [Knowledge Maps](maps.md).

## Contents

- [Linear Programming](#linear-programming)
- [Integer Programming and Mixed-Integer Programming](#integer-programming-and-mixed-integer-programming)
- [Nonlinear Programming](#nonlinear-programming)
- [Convex Optimization](#convex-optimization)
- [Combinatorial Optimization](#combinatorial-optimization)
- [Network Optimization](#network-optimization)
- [Dynamic Programming](#dynamic-programming)
- [Stochastic Programming](#stochastic-programming)
- [Robust Optimization](#robust-optimization)
- [Queueing Theory](#queueing-theory)
- [Simulation](#simulation)
- [Inventory Theory](#inventory-theory)
- [Scheduling](#scheduling)
- [Vehicle Routing and Logistics](#vehicle-routing-and-logistics)
- [Facility Location](#facility-location)
- [Decision Analysis](#decision-analysis)
- [Game Theory](#game-theory)
- [Constraint Programming](#constraint-programming)
- [Metaheuristics](#metaheuristics)
- [Multi-Objective Optimization](#multi-objective-optimization)
- [Decomposition Methods](#decomposition-methods)

## Linear Programming

Linear programming optimizes a linear objective subject to linear constraints.

- Best beginner resources: [MIT 15.053](courses.md#introductory-operations-research), [Applied Mathematical Programming](books.md#modeling-and-mathematical-programming), and [Linear Programming: Foundations and Extensions](books.md#linear-and-integer-programming).
- Key books: [Introduction to Linear Optimization](books.md#linear-and-integer-programming), [Linear Programming and Network Flows](books.md#linear-and-integer-programming), and [Theory of Linear and Integer Programming](books.md#linear-and-integer-programming).
- Key courses: [Linear Programming](courses.md#linear-programming) and [Network Optimization](courses.md#network-optimization).
- Key papers: [Linear Programming and the Simplex Method](papers.md#linear-programming-and-the-simplex-method).
- Software/tools: [HiGHS](softwares.md#open-source-solvers), [CLP](softwares.md#open-source-solvers), [Gurobi](softwares.md#commercial-solvers), [CPLEX](softwares.md#commercial-solvers), [Pyomo](libraries.md#python), [JuMP](libraries.md#julia), and [PuLP](libraries.md#python).
- Datasets/benchmarks: [Netlib LP](datasets.md#optimization-benchmarks) and [Mittelmann benchmarks](datasets.md#optimization-benchmarks).

## Integer Programming and Mixed-Integer Programming

Integer programming adds discrete decisions, usually binary or integer variables, to optimization models.

- Best beginner resources: [Model Building in Mathematical Programming](books.md#modeling-and-mathematical-programming), [Coursera Discrete Optimization](courses.md#integer-and-combinatorial-optimization), and [Gurobi modeling examples](tutorials.md#gurobi-tutorials).
- Key books: [Integer Programming](books.md#linear-and-integer-programming), [Integer and Combinatorial Optimization](books.md#linear-and-integer-programming), and [Optimization over Integers](books.md#linear-and-integer-programming).
- Key papers: [Integer Programming](papers.md#integer-programming), [Branch and Bound](papers.md#integer-programming), and [Decomposition Methods](papers.md#decomposition-methods).
- Software/tools: [Gurobi](solver-comparison.md#solver-notes), [CPLEX](solver-comparison.md#solver-notes), [Xpress](solver-comparison.md#solver-notes), [SCIP](solver-comparison.md#solver-notes), [HiGHS](solver-comparison.md#solver-notes), and [CBC](solver-comparison.md#solver-notes).
- Datasets/benchmarks: [MIPLIB](datasets.md#optimization-benchmarks), [OR-Library](datasets.md#optimization-benchmarks), and [Mittelmann benchmarks](datasets.md#optimization-benchmarks).
- Researchers/communities: [Integer Programming researchers](researchers.md#integer-programming), [IPCO](events.md#optimization-and-mathematical-programming-conferences), and [Mathematical Optimization Society](events.md#professional-societies).

## Nonlinear Programming

Nonlinear programming optimizes nonlinear objectives or constraints, with or without convexity.

- Best beginner resources: [Numerical Optimization](books.md#nonlinear-and-convex-optimization), [SciPy Optimize](libraries.md#python), and [CasADi](libraries.md#python).
- Key books: [Numerical Optimization](books.md#nonlinear-and-convex-optimization), [Introduction to Nonlinear Optimization](books.md#nonlinear-and-convex-optimization), and [Practical Optimization](books.md#nonlinear-and-convex-optimization).
- Key courses: [Convex Optimization](courses.md#convex-optimization) and continuous optimization courses in [Courses](courses.md).
- Software/tools: [Ipopt](softwares.md#open-source-solvers), [Artelys Knitro](softwares.md#commercial-solvers), [SCIP](softwares.md#open-source-solvers), [CasADi](libraries.md#python), [Pyomo](libraries.md#python), and [JuMP](libraries.md#julia).
- Datasets/benchmarks: [MINLPLib](datasets.md#optimization-benchmarks) and [QPLIB](datasets.md#optimization-benchmarks).

## Convex Optimization

Convex optimization studies problems where local optima are global optima under convex structure.

- Best beginner resources: [Convex Optimization](books.md#nonlinear-and-convex-optimization), [Stanford EE364a](courses.md#convex-optimization), and [CVXPY Short Course](tutorials.md#convex-optimization-tutorials).
- Key books: Boyd and Vandenberghe, Bertsekas, Ben-Tal and Nemirovski, and the [MOSEK Modeling Cookbook](books.md#modeling-and-mathematical-programming).
- Key papers: [Linear Programming and Interior-Point Methods](papers.md#linear-programming-and-the-simplex-method) and robust convex optimization papers in [Robust Optimization](papers.md#robust-optimization).
- Software/tools: [CVXPY](libraries.md#python), [CVXR](libraries.md#r), [Convex.jl](libraries.md#julia), [MOSEK](softwares.md#commercial-solvers), [SCS](softwares.md#open-source-solvers), [ECOS](softwares.md#open-source-solvers), and [OSQP](softwares.md#open-source-solvers).
- Communities: [SIAM Activity Group on Optimization](events.md#professional-societies) and [Optimization Online](blogs.md#optimization-blogs).

## Combinatorial Optimization

Combinatorial optimization studies optimization over discrete structures such as graphs, sets, schedules, routes, and matchings.

- Best beginner resources: [Discrete Optimization](courses.md#integer-and-combinatorial-optimization), [Algorithms for OR](courses.md#algorithms-for-or), and [The Design of Approximation Algorithms](books.md#metaheuristics-and-approximation).
- Key books: [Combinatorial Optimization](books.md#network-flows-and-combinatorial-optimization), Schrijver, Korte and Vygen, and Papadimitriou and Steiglitz.
- Key papers: [Approximation and Heuristics](papers.md#approximation-and-heuristics).
- Software/tools: [OR-Tools](softwares.md#open-source-solvers), [SCIP](softwares.md#open-source-solvers), [MiniZinc](softwares.md#modeling-languages-and-algebraic-modeling-systems), [Timefold](softwares.md#constraint-programming-tools), and graph libraries in [Libraries](libraries.md).
- Datasets/benchmarks: [OR-Library](datasets.md#optimization-benchmarks), [DIMACS Challenges](datasets.md#optimization-benchmarks), and [MiniZinc Challenge](datasets.md#optimization-benchmarks).

## Network Optimization

Network optimization models flows, paths, cuts, matchings, and connected systems.

- Best beginner resources: [Network Flows](books.md#network-flows-and-combinatorial-optimization), [Network Optimization courses](courses.md#network-optimization), and [NetworkX](libraries.md#python).
- Key books: Ahuja, Magnanti, and Orlin; Bazaraa, Jarvis, and Sherali; and Williamson.
- Key papers: [Network Flows](papers.md#network-flows).
- Software/tools: [NetworkX](libraries.md#python), [Graphs.jl](libraries.md#julia), [JGraphT](libraries.md#java), [OR-Tools](softwares.md#open-source-solvers), and commercial MIP solvers.
- Datasets/benchmarks: [DIMACS Challenges](datasets.md#optimization-benchmarks) and [TransportationNetworks](datasets.md#transportation-and-routing-datasets).

## Dynamic Programming

Dynamic programming solves problems by decomposing them into states, actions, transitions, and value functions.

- Best beginner resources: [Bertsekas videos](courses.md#decision-analysis), [Dynamic Programming and Optimal Control](books.md#decision-analysis-and-game-theory), and [AI and OR](ai-and-or.md#reinforcement-learning).
- Key books: Bertsekas and Puterman.
- Key papers: [Dynamic Programming](papers.md#dynamic-programming).
- Software/tools: Python, Julia, reinforcement learning libraries, custom implementations, and simulation environments.
- Related areas: [Reinforcement Learning](ai-and-or.md#reinforcement-learning), stochastic control, inventory control, and Markov decision processes.

## Stochastic Programming

Stochastic programming optimizes decisions under uncertainty using scenarios, recourse, and probability models.

- Best beginner resources: [Introduction to Stochastic Programming](books.md#stochastic-programming-and-robust-optimization) and [Stochastic Programming Lectures](courses.md#stochastic-models).
- Key books: Birge and Louveaux; Shapiro, Dentcheva, and Ruszczynski; King and Wallace.
- Key papers: [Stochastic Programming](papers.md#stochastic-programming).
- Software/tools: [Pyomo](libraries.md#python), [JuMP](libraries.md#julia), [StochasticPrograms.jl](libraries.md#julia), [SDDP.jl](libraries.md#julia), and commercial MIP solvers.
- Datasets/benchmarks: scenario datasets from [Datasets](datasets.md), MIPLIB, and application-specific data.

## Robust Optimization

Robust optimization seeks decisions that perform well across uncertainty sets rather than relying on exact probability distributions.

- Best beginner resources: [Robust Optimization](books.md#stochastic-programming-and-robust-optimization), [MOSEK Modeling Cookbook](books.md#modeling-and-mathematical-programming), and [Stanford EE364b](courses.md#convex-optimization).
- Key papers: [Robust Optimization](papers.md#robust-optimization).
- Software/tools: [JuMP](libraries.md#julia), [Pyomo](libraries.md#python), [CVXPY](libraries.md#python), [MOSEK](softwares.md#commercial-solvers), and MIP/conic solvers.
- Applications: supply chain resilience, energy, finance, healthcare, and transportation.

## Queueing Theory

Queueing theory models congestion, waiting, capacity, and service systems.

- Best beginner resources: [Fundamentals of Queueing Theory](books.md#queueing-theory), [MIT 6.262](courses.md#queueing-theory), and [NPTEL Queueing Systems](courses.md#queueing-theory).
- Key papers: [Queueing Theory](papers.md#queueing-theory).
- Software/tools: analytical formulas, simulation with [SimPy](libraries.md#python), [simmer](libraries.md#r), and discrete-event simulation packages.
- Datasets: [Call Center Data](datasets.md#simulation-and-queueing-datasets) and healthcare/service datasets.
- Applications: call centers, hospitals, telecommunications, computing systems, and transportation.

## Simulation

Simulation evaluates systems through computational experiments when analytical models are difficult or incomplete.

- Discrete-event simulation: events, resources, queues, and process flows; see [SimPy](softwares.md#simulation-software), [Arena](softwares.md#simulation-software), [Simio](softwares.md#simulation-software), and [AnyLogic](softwares.md#simulation-software).
- Monte Carlo simulation: random sampling for uncertainty, risk, and statistical estimation.
- Agent-based simulation: autonomous agents interacting under behavioral rules; common in mobility, epidemics, markets, and policy.
- System dynamics: feedback loops, stocks, flows, and aggregate dynamic behavior.
- Best beginner resources: [Simulation books](books.md#simulation), [Simulation courses](courses.md#simulation), and [Simulation tutorials](tutorials.md#simulation-tutorials).
- Key papers: [Simulation](papers.md#simulation).
- Conferences: [Winter Simulation Conference](events.md#simulation-conferences).

## Inventory Theory

Inventory theory determines how much stock to hold, when to reorder, and how to balance service and cost.

- Best beginner resources: [Inventory and Supply Chain books](books.md#inventory-and-supply-chain), [Supply Chain and Inventory courses](courses.md#supply-chain-and-inventory), and [Supply Chain Analyst path](learning-paths.md#supply-chain-analyst).
- Key models: EOQ, newsvendor, base-stock policies, multi-echelon inventory, stochastic demand, and service levels.
- Key papers: [Inventory Theory](papers.md#inventory-theory).
- Software/tools: spreadsheets, Python/R simulation, [Pyomo](libraries.md#python), [JuMP](libraries.md#julia), and commercial solvers.
- Applications: retail, manufacturing, spare parts, healthcare supplies, and humanitarian logistics.

## Scheduling

Scheduling allocates jobs, people, machines, rooms, vehicles, or crews over time.

- Best beginner resources: [Scheduling books](books.md#scheduling), [Scheduling courses](courses.md#scheduling), and [OR-Tools Scheduling Guides](tutorials.md#scheduling-tutorials).
- Key papers: [Scheduling](papers.md#scheduling).
- Software/tools: [OR-Tools CP-SAT](softwares.md#constraint-programming-tools), [MiniZinc](softwares.md#constraint-programming-tools), [Timefold](softwares.md#constraint-programming-tools), [Choco](softwares.md#constraint-programming-tools), [CPLEX CP Optimizer](softwares.md#constraint-programming-tools), and MIP solvers.
- Datasets/benchmarks: [PSPLIB](datasets.md#scheduling-benchmarks), [Taillard instances](datasets.md#scheduling-benchmarks), and OR-Library scheduling instances.

## Vehicle Routing and Logistics

Vehicle routing determines efficient routes under capacity, time, pickup-delivery, and service constraints.

- Best beginner resources: [OR-Tools Routing Guides](tutorials.md#routing-tutorials), [Vehicle Routing](books.md#network-flows-and-combinatorial-optimization), and [Transportation and Routing applications](applications.md#transportation-and-routing).
- Key papers: [Vehicle Routing and Logistics](papers.md#vehicle-routing-and-logistics).
- Software/tools: [OR-Tools](softwares.md#open-source-solvers), [Hexaly](solver-comparison.md#solver-notes), [Gurobi](solver-comparison.md#solver-notes), [SCIP](solver-comparison.md#solver-notes), and route-optimization APIs.
- Datasets/benchmarks: [CVRPLIB](datasets.md#transportation-and-routing-datasets), [TSPLIB](datasets.md#optimization-benchmarks), and [Solomon VRPTW](datasets.md#transportation-and-routing-datasets).

## Facility Location

Facility location chooses sites for warehouses, clinics, plants, depots, or services under cost, coverage, and capacity tradeoffs.

- Best beginner resources: [Applications](applications.md), [Supply Chain and Logistics](industry-guides.md#supply-chain-and-logistics), and [Public Sector and Policy](industry-guides.md#public-sector-and-policy).
- Key books: [Location science references](papers.md#facility-location) and supply chain network design books in [Books](books.md#inventory-and-supply-chain).
- Key papers: [Facility Location](papers.md#facility-location).
- Software/tools: MIP solvers, [Pyomo](libraries.md#python), [JuMP](libraries.md#julia), [Gurobi](solver-comparison.md#solver-notes), and [CPLEX](solver-comparison.md#solver-notes).
- Datasets: OR-Library, public GIS data, demand points, and open-data portals.

## Decision Analysis

Decision analysis formalizes choices under uncertainty, preferences, risk, and value of information.

- Best beginner resources: [Decision Analysis books](books.md#decision-analysis-and-game-theory), [MIT 15.060](courses.md#decision-analysis), and [Decision Analysis journal](journals.md#flagship-or-journals).
- Key methods: decision trees, influence diagrams, expected utility, value of information, multi-criteria decision analysis, and risk analysis.
- Software/tools: spreadsheets, decision-tree tools, simulation, Bayesian models, and optimization models.
- Communities: [INFORMS Decision Analysis Society](https://connect.informs.org/das/home) and [Decision Analysis](journals.md#flagship-or-journals).

## Game Theory

Game theory studies strategic interactions among decision-makers.

- Best beginner resources: [Algorithmic Game Theory](books.md#decision-analysis-and-game-theory), [Decision Analysis and Game Theory books](books.md#decision-analysis-and-game-theory), and [Foundations papers](papers.md#foundations-of-operations-research).
- Key methods: Nash equilibrium, cooperative games, mechanism design, auctions, matching, and stochastic games.
- Software/tools: custom computational models, optimization solvers, simulation, and game-theory packages.
- Applications: markets, revenue management, transportation, defense, public policy, and networks.

## Constraint Programming

Constraint programming models combinatorial decisions through variables, domains, constraints, and search.

- Best beginner resources: [MiniZinc Handbook](tutorials.md#scheduling-tutorials), [Constraint Programming course](courses.md#scheduling), and [CPAIOR](events.md#optimization-and-mathematical-programming-conferences).
- Software/tools: [MiniZinc](softwares.md#constraint-programming-tools), [OR-Tools CP-SAT](softwares.md#constraint-programming-tools), [Choco Solver](softwares.md#constraint-programming-tools), [Timefold](softwares.md#constraint-programming-tools), and [CP Optimizer](softwares.md#constraint-programming-tools).
- Datasets/benchmarks: [MiniZinc Challenge](datasets.md#optimization-benchmarks) and [XCSP Competition](competitions.md#constraint-programming-competitions).
- Applications: scheduling, timetabling, rostering, routing, configuration, and planning.

## Metaheuristics

Metaheuristics provide flexible approximate search methods for difficult optimization problems.

- Best beginner resources: [Essentials of Metaheuristics](books.md#metaheuristics-and-approximation), [Metaheuristics courses](courses.md#integer-and-combinatorial-optimization), and [DEAP](libraries.md#python).
- Key methods: local search, tabu search, simulated annealing, genetic algorithms, ant colony optimization, particle swarm optimization, and large neighborhood search.
- Software/tools: [DEAP](libraries.md#python), [pymoo](libraries.md#python), [BlackBoxOptim.jl](libraries.md#julia), [OR-Tools](softwares.md#open-source-solvers), and custom implementations.
- Datasets/benchmarks: routing, scheduling, and OR-Library benchmarks.

## Multi-Objective Optimization

Multi-objective optimization handles tradeoffs among multiple competing goals.

- Best beginner resources: [pymoo](libraries.md#python), [Decision Analysis](books.md#decision-analysis-and-game-theory), and [MOSEK Modeling Cookbook](books.md#modeling-and-mathematical-programming).
- Key methods: Pareto efficiency, weighted sums, epsilon-constraint methods, goal programming, evolutionary multi-objective algorithms, and interactive decision-making.
- Software/tools: [pymoo](libraries.md#python), [JuMP](libraries.md#julia), [Pyomo](libraries.md#python), [CVXPY](libraries.md#python), and solver APIs.
- Applications: energy, public policy, supply chain, healthcare, and portfolio optimization.

## Decomposition Methods

Decomposition methods exploit structure to solve large-scale optimization models.

- Benders decomposition: separates complicating variables from subproblem structure; see [Benders papers](papers.md#decomposition-methods).
- Dantzig-Wolfe decomposition: reformulates structured LP/MIP problems using columns; see [Dantzig-Wolfe](papers.md#decomposition-methods).
- Column generation: generates variables dynamically, often used in crew scheduling, vehicle routing, and cutting stock.
- Lagrangian relaxation: relaxes difficult constraints with multipliers to obtain bounds and decomposable subproblems.
- Best beginner resources: [Decomposition Techniques in Mathematical Programming](books.md#linear-and-integer-programming), [Branch-and-Price](papers.md#decomposition-methods), and advanced optimization courses.
- Software/tools: [JuMP](libraries.md#julia), [Pyomo](libraries.md#python), [SCIP](softwares.md#open-source-solvers), [Gurobi](softwares.md#commercial-solvers), [CPLEX](softwares.md#commercial-solvers), and custom algorithm code.
