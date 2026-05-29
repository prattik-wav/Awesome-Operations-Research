# Operations Research Curriculum

A suggested learning roadmap for Operations Research. Use it as a guide for self-study, course planning, professional upskilling, or curriculum design.

## Contents

- [Beginner Path](#beginner-path)
- [Intermediate Path](#intermediate-path)
- [Advanced Path](#advanced-path)
- [Application Tracks](#application-tracks)
- [Suggested Semester Course Sequences](#suggested-semester-course-sequences)
- [Practice Milestones](#practice-milestones)

## Beginner Path

Learn the language of models and decisions.

- Mathematical modeling - Decision variables, objectives, constraints, data, assumptions, and model validation.
- Linear programming - Formulation, graphical intuition, simplex basics, duality, and sensitivity analysis.
- Spreadsheet optimization - Excel Solver or OpenSolver for small LP and integer models.
- Probability and statistics - Random variables, expectation, variance, confidence intervals, and regression basics.
- Programming - Introductory Python, R, or Julia for data handling and reproducible modeling.
- Simulation basics - Random sampling, discrete-event simulation concepts, and output analysis.
- Core applications - Product mix, blending, assignment, transportation, shortest path, inventory, and basic queueing models.

Recommended practice:

- Implement small LP models in a spreadsheet and in Python or Julia.
- Solve assignment, transportation, and network flow examples.
- Build a simple discrete-event queue simulation.

## Intermediate Path

Move from clean textbook models to realistic models and computational practice.

- Integer programming - Binary variables, logical constraints, big-M modeling, branch-and-bound, branch-and-cut, and model strengthening.
- Network models - Shortest path, minimum spanning tree, max flow, min-cost flow, matching, and facility location.
- Queueing theory - M/M/1, M/M/c, finite queues, networks of queues, and service-system design.
- Inventory models - EOQ, newsvendor, base-stock policies, stochastic demand, and multi-echelon intuition.
- Simulation modeling - Discrete-event simulation, random number generation, warm-up, replications, and variance reduction.
- Decision analysis - Decision trees, value of information, utility, risk, and multi-criteria decision-making.
- Heuristics - Local search, greedy methods, tabu search, simulated annealing, genetic algorithms, and large neighborhood search.
- Python-based modeling - Pyomo, PuLP, OR-Tools, CVXPY, or JuMP for solver-backed models.

Recommended practice:

- Model a routing, scheduling, or facility location problem with real or benchmark data.
- Compare exact and heuristic methods on the same problem.
- Write clear assumptions and validation notes for every model.

## Advanced Path

Study theory, large-scale computation, uncertainty, and modern integrations.

- Convex optimization - Convex sets and functions, KKT conditions, duality, conic optimization, and interior-point methods.
- Nonlinear programming - Unconstrained and constrained methods, SQP, interior-point NLP, global optimization, and derivative-free methods.
- Stochastic programming - Two-stage models, multi-stage models, recourse, sample average approximation, and stochastic dual dynamic programming.
- Robust optimization - Uncertainty sets, robust counterparts, adjustable robustness, distributionally robust optimization, and conservatism tradeoffs.
- Decomposition methods - Dantzig-Wolfe decomposition, column generation, Benders decomposition, Lagrangian relaxation, and branch-and-price.
- Large-scale optimization - Sparse linear algebra, presolve, cuts, warm starts, parallelism, and numerical reliability.
- Computational complexity - NP-hardness, reductions, approximation algorithms, and integrality gaps.
- Advanced simulation - Ranking and selection, metamodeling, simulation optimization, and agent-based simulation.
- Machine learning and OR - Predict-then-optimize, decision-focused learning, reinforcement learning, learned heuristics, and ML-assisted solvers.

Recommended practice:

- Reproduce a published model or benchmark study.
- Implement a decomposition method on a structured problem.
- Combine prediction with optimization and evaluate decision quality, not just prediction error.

## Application Tracks

### Supply Chain and Logistics

- Demand forecasting, inventory control, network design, vehicle routing, warehouse operations, and resilience.
- Tools: Pyomo, JuMP, OR-Tools, Gurobi, CPLEX, AnyLogic, SimPy.

### Healthcare Systems

- Appointment scheduling, operating room planning, patient flow, staffing, emergency response, and resource allocation.
- Tools: discrete-event simulation, stochastic programming, queueing, integer programming, and Markov decision processes.

### Manufacturing Systems

- Production planning, lot sizing, machine scheduling, maintenance, quality control, and facility layout.
- Tools: MIP, CP-SAT, simulation, digital twins, and stochastic models.

### Energy Systems

- Unit commitment, economic dispatch, capacity expansion, optimal power flow, storage, and renewable integration.
- Tools: JuMP, Pyomo, PowerModels.jl, MATPOWER, stochastic and robust optimization.

### Transportation

- Traffic assignment, transit planning, fleet management, routing, network design, and mobility analytics.
- Tools: network optimization, simulation, VRP heuristics, and geographic data analysis.

### Finance

- Portfolio optimization, risk management, asset-liability management, market making, and revenue management.
- Tools: convex optimization, stochastic programming, robust optimization, and dynamic programming.

### Public Policy

- Resource allocation, emergency services, infrastructure planning, voting systems, fairness-aware allocation, and regulation.
- Tools: integer programming, decision analysis, simulation, game theory, and multi-objective optimization.

### Humanitarian Operations

- Disaster response, relief distribution, evacuation planning, food systems, and public health logistics.
- Tools: facility location, routing, stochastic programming, robust optimization, and simulation.

## Suggested Semester Course Sequences

### Undergraduate OR Minor

1. Calculus, linear algebra, probability, and statistics.
2. Introductory programming for analytics.
3. Introduction to Operations Research.
4. Linear and integer programming.
5. Simulation or stochastic models.
6. Applied elective: supply chain, healthcare, transportation, manufacturing, or analytics.

### Master's-Level OR Concentration

1. Optimization modeling and linear programming.
2. Integer and combinatorial optimization.
3. Stochastic processes and queueing.
4. Simulation modeling and analysis.
5. Nonlinear or convex optimization.
6. Application studio or capstone with real data and stakeholder communication.

### PhD-Level OR Preparation

1. Real analysis, linear algebra, probability theory, and algorithms.
2. Convex analysis and nonlinear optimization.
3. Integer programming and polyhedral theory.
4. Stochastic programming, dynamic programming, or stochastic control.
5. Decomposition, large-scale computation, and complexity.
6. Research seminar, paper replication, and original thesis problem development.

### Self-Study Path for Practitioners

1. Learn modeling fundamentals with spreadsheet optimization and a short OR textbook.
2. Pick one programming stack: Python with Pyomo/OR-Tools/CVXPY or Julia with JuMP.
3. Solve small benchmark problems and inspect solver logs.
4. Study the application domain you actually work in.
5. Add uncertainty through simulation, stochastic models, or robust optimization.
6. Build a decision-support prototype with documentation, sensitivity analysis, and clear limitations.

## Practice Milestones

- Beginner - Formulate and solve a clean LP, transportation model, and assignment model.
- Intermediate - Build a MIP model with binary logic and validate it against benchmark or historical data.
- Advanced - Implement a decomposition, heuristic, or simulation optimization workflow and explain its computational tradeoffs.
- Professional - Deliver a model that a domain stakeholder can use, audit, and maintain.
