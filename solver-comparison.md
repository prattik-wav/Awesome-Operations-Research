# Solver Comparison Guide

High-level comparison of major optimization solvers. Capabilities and licensing change over time, so verify details with vendor or project documentation before procurement or production deployment.

## Contents

- [Quick Selection Guide](#quick-selection-guide)
- [Capability Matrix](#capability-matrix)
- [Licensing and Deployment](#licensing-and-deployment)
- [Solver Notes](#solver-notes)
- [Common Abbreviations](#common-abbreviations)

## Quick Selection Guide

- Best commercial MIP shortlist: [Gurobi](https://www.gurobi.com/), [IBM CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio), [FICO Xpress](https://www.fico.com/en/products/fico-xpress-optimization), [COPT](https://www.shanshu.ai/copt), and [Hexaly](https://www.hexaly.com/).
- Best open-source LP/MIP starting point: [HiGHS](https://highs.dev/), [SCIP](https://www.scipopt.org/), and [CBC](https://github.com/coin-or/Cbc).
- Best conic optimization shortlist: [MOSEK](https://www.mosek.com/), [SCS](https://www.cvxgrp.org/scs/), [ECOS](https://github.com/embotech/ecos), and solver backends through [CVXPY](https://www.cvxpy.org/).
- Best nonlinear optimization shortlist: [Ipopt](https://coin-or.github.io/Ipopt/), [Artelys Knitro](https://www.artelys.com/solvers/knitro/), [SCIP](https://www.scipopt.org/), [Gurobi](https://www.gurobi.com/), and [CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio) for supported nonconvex quadratic classes.
- Best routing and scheduling starting point: [OR-Tools CP-SAT](https://developers.google.com/optimization/cp/cp_solver), [Hexaly](https://www.hexaly.com/), [Timefold](https://timefold.ai/), and commercial MIP/CP solvers.

## Capability Matrix

| Solver | LP | MIP | NLP | QP | MIQP | SOCP | SDP | Licensing | Academic license | Speed and commercial usage |
|---|---|---|---|---|---|---|---|---|---|---|
| Gurobi | Yes | Yes | Limited nonlinear and nonconvex quadratic classes | Yes | Yes | Limited/conic via supported quadratic forms | No general SDP | Commercial | Free academic licenses available | Top-tier commercial LP/MIP/QP speed; widely used in industry. |
| IBM CPLEX | Yes | Yes | CP Optimizer and supported nonlinear/quadratic classes | Yes | Yes | Yes for selected conic forms | No general SDP | Commercial | Academic access available through IBM programs | Top-tier commercial LP/MIP/QP/CP ecosystem; strong enterprise support. |
| SCIP | Yes via LP backends | Yes | Yes for MINLP classes | Yes via interfaces/backends | Yes for supported models | Limited via reformulation/backend | No general SDP | Open-source Apache 2.0 for SCIP 9+; check dependencies | Free for academic and open-source use | Strong open-source MIP/MINLP research solver; production use depends on deployment needs. |
| HiGHS | Yes | Yes | No | Convex QP | No general MIQP | No | No | MIT open-source | Open-source | Excellent open-source LP and growing MIP/QP capability. |
| CBC | Yes via CLP | Yes | No | Limited | Limited | No | No | EPL open-source | Open-source | Reliable open-source MIP baseline; often slower than leading commercial solvers. |
| GLPK | Yes | Yes | No | No | No | No | No | GPL open-source | Open-source | Useful for teaching and small models; generally not a high-performance MIP solver. |
| FICO Xpress | Yes | Yes | Yes for supported classes | Yes | Yes | Yes | Limited/no general SDP | Commercial | Academic programs available | Top-tier commercial optimization suite with modeling, MIP, and deployment tools. |
| MOSEK | Yes | Yes for mixed-integer conic classes | Convex nonlinear through conic forms | Yes | Yes for supported convex classes | Yes | Yes | Commercial | Free academic licenses available | Excellent conic and convex optimization solver; strong in SOCP/SDP/exponential/power cones. |
| COPT | Yes | Yes | Limited supported classes | Yes | Yes | Yes | No general SDP | Commercial | Academic licenses available | High-performance commercial LP/MIP/QP/SOCP solver; increasingly used in enterprise settings. |
| Hexaly | Yes | Yes | Yes for many nonlinear/discrete models | Yes | Yes | No general conic focus | No | Commercial | Academic licenses available | Strong for large-scale routing, scheduling, nonlinear, and combinatorial optimization. |

## Licensing and Deployment

- Open-source permissive: HiGHS and modern SCIP releases are attractive for redistribution-friendly deployments; always check dependency licenses.
- Open-source copyleft: GLPK is GPL, which may affect embedding in proprietary software.
- Commercial: Gurobi, CPLEX, Xpress, MOSEK, COPT, and Hexaly usually offer academic licenses, evaluation licenses, and paid commercial licenses.
- Cloud deployment: verify container, server, token, floating license, and SaaS restrictions before designing a service.
- Reproducibility: record solver version, parameters, platform, time limits, gaps, random seeds, and presolve settings.

## Solver Notes

- [CBC](https://github.com/coin-or/Cbc) - Good open-source MIP baseline; commonly available through PuLP, Pyomo, JuMP, and OpenSolver.
- [COPT](https://www.shanshu.ai/copt) - Commercial solver for LP, MIP, QP, QCP, SOCP, and related optimization models.
- [CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio) - Mature commercial optimizer with CPLEX, CP Optimizer, OPL, Python APIs, and enterprise integration.
- [GLPK](https://www.gnu.org/software/glpk/) - Useful for teaching and GNU workflows; less competitive on large MIP benchmarks.
- [Gurobi](https://www.gurobi.com/) - Widely used commercial optimizer with strong APIs, documentation, examples, and academic access.
- [Hexaly](https://www.hexaly.com/) - Commercial solver formerly known as LocalSolver; often used for large-scale combinatorial, routing, and scheduling problems.
- [HiGHS](https://highs.dev/) - Modern open-source solver with strong LP performance and active MIP development.
- [MOSEK](https://www.mosek.com/) - Excellent for conic optimization, convex QP, SOCP, SDP, exponential cones, and power cones.
- [SCIP](https://www.scipopt.org/) - Research-grade and practical MIP/MINLP framework with plugins, branch-cut-and-price capabilities, and strong modeling interfaces.
- [Xpress](https://www.fico.com/en/products/fico-xpress-optimization) - Commercial optimization suite with solver, Mosel modeling, and enterprise tooling.

## Common Abbreviations

- LP - Linear programming.
- MIP - Mixed-integer linear programming.
- NLP - Nonlinear programming.
- QP - Quadratic programming.
- MIQP - Mixed-integer quadratic programming.
- SOCP - Second-order cone programming.
- SDP - Semidefinite programming.
- MINLP - Mixed-integer nonlinear programming.
- CP - Constraint programming.
