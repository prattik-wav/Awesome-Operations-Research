# Modeling Language Comparison

Comparison of common algebraic and domain-specific modeling tools for Operations Research.

## Contents

- [Comparison Table](#comparison-table)
- [Syntax Examples](#syntax-examples)
- [Language Notes](#language-notes)
- [Selection Advice](#selection-advice)

## Comparison Table

| Tool | Style | Strengths | Weaknesses | Solver support |
|---|---|---|---|---|
| [AMPL](https://ampl.com/) | Algebraic modeling language | Clean syntax, mature solver ecosystem, strong commercial support, excellent for teaching and deployment. | Commercial for many uses; separate language from host programming environments. | Very broad commercial and open-source solver support. |
| [GAMS](https://www.gams.com/) | Algebraic modeling system | Large-scale modeling, equilibrium models, energy/economic models, mature data handling. | Commercial; syntax can feel specialized to newcomers. | Very broad solver support. |
| [JuMP](https://jump.dev/) | Julia-embedded modeling | Fast, expressive, excellent solver abstraction, strong nonlinear and conic support. | Requires Julia adoption; package ecosystem differs from Python. | Broad support through MathOptInterface. |
| [Pyomo](https://www.pyomo.org/) | Python-embedded algebraic modeling | Flexible Python integration, strong for research, stochastic programming, and complex workflows. | Can be slower to build very large models than lower-level APIs; requires careful Python modeling practice. | Broad LP/MIP/NLP support through solver plugins. |
| [CVXPY](https://www.cvxpy.org/) | Python-embedded convex modeling | Disciplined convex programming, conic modeling, differentiable optimization ecosystem. | Only models problems that satisfy supported disciplined programming rules unless using extensions. | Strong conic and convex solver support. |
| [PuLP](https://coin-or.github.io/pulp/) | Python LP/MIP modeling | Simple, lightweight, friendly for teaching and small-to-medium LP/MIP models. | Less expressive for nonlinear, stochastic, or complex large-scale modeling. | CBC by default; commercial and open-source LP/MIP solvers via interfaces. |
| [AIMMS](https://www.aimms.com/) | Commercial modeling and app platform | Optimization applications, dashboards, deployment, supply chain decision apps. | Commercial; heavier platform than code-first tools. | Commercial and open-source solver integrations. |
| [OPL](https://www.ibm.com/docs/en/icos) | IBM optimization modeling language | Tight CPLEX/CP Optimizer integration, good for MIP and CP teaching. | Mostly tied to IBM ecosystem. | CPLEX and CP Optimizer. |
| [MiniZinc](https://www.minizinc.org/) | Constraint modeling language | Solver-independent CP modeling, challenges, benchmarks, and compact combinatorial models. | Less natural for general algebraic large-scale LP workflows. | CP, MIP, SAT, and FlatZinc-compatible solvers. |

## Syntax Examples

### AMPL

```ampl
set PRODUCTS;
param profit{PRODUCTS};
param demand{PRODUCTS};
var x{p in PRODUCTS} >= 0;
maximize TotalProfit: sum{p in PRODUCTS} profit[p] * x[p];
subject to DemandLimit{p in PRODUCTS}: x[p] <= demand[p];
```

### GAMS

```gams
Sets p products;
Parameters profit(p), demand(p);
Positive Variables x(p);
Variable z;
Equations obj, limit(p);
obj.. z =e= sum(p, profit(p) * x(p));
limit(p).. x(p) =l= demand(p);
Model m /all/;
Solve m using lp maximizing z;
```

### JuMP

```julia
using JuMP, HiGHS
model = Model(HiGHS.Optimizer)
@variable(model, x[p in products] >= 0)
@objective(model, Max, sum(profit[p] * x[p] for p in products))
@constraint(model, [p in products], x[p] <= demand[p])
optimize!(model)
```

### Pyomo

```python
import pyomo.environ as pyo
m = pyo.ConcreteModel()
m.P = pyo.Set(initialize=products)
m.x = pyo.Var(m.P, domain=pyo.NonNegativeReals)
m.obj = pyo.Objective(expr=sum(profit[p] * m.x[p] for p in m.P), sense=pyo.maximize)
m.limit = pyo.Constraint(m.P, rule=lambda m, p: m.x[p] <= demand[p])
pyo.SolverFactory("highs").solve(m)
```

### CVXPY

```python
import cvxpy as cp
x = cp.Variable(n, nonneg=True)
problem = cp.Problem(cp.Maximize(profit @ x), [x <= demand])
problem.solve()
```

### PuLP

```python
import pulp
model = pulp.LpProblem("product_mix", pulp.LpMaximize)
x = {p: pulp.LpVariable(f"x_{p}", lowBound=0) for p in products}
model += pulp.lpSum(profit[p] * x[p] for p in products)
for p in products:
    model += x[p] <= demand[p]
model.solve()
```

### MiniZinc

```minizinc
set of int: PRODUCTS;
array[PRODUCTS] of float: profit;
array[PRODUCTS] of float: demand;
array[PRODUCTS] of var 0.0..max(demand): x;
constraint forall(p in PRODUCTS)(x[p] <= demand[p]);
solve maximize sum(p in PRODUCTS)(profit[p] * x[p]);
```

## Language Notes

- AMPL - Excellent for clear mathematical models, solver experimentation, and teaching algebraic modeling.
- GAMS - Strong in energy, economics, equilibrium, and large multi-scenario models.
- JuMP - Often the best choice for Julia users building high-performance research and production optimization workflows.
- Pyomo - Often the best choice for Python users needing general algebraic modeling and integration with data pipelines.
- CVXPY - Best when the problem is convex and naturally expressed with matrix operations.
- PuLP - Best for lightweight LP/MIP examples, prototypes, and teaching.
- AIMMS - Best for full decision-support applications where users need interfaces, deployment, and scenario management.
- OPL - Best inside the IBM optimization ecosystem, especially for CPLEX and CP Optimizer.
- MiniZinc - Best for finite-domain combinatorial models, CP benchmarks, and solver-independent CP experimentation.

## Selection Advice

- Choose by problem class first: LP/MIP, conic, nonlinear, CP, simulation, or hybrid.
- Choose by workflow second: notebook, production service, desktop app, teaching, or enterprise decision app.
- Choose by solver access third: commercial solver, open-source solver, cloud license, or academic license.
- For long-lived projects, prototype in a modeling language but preserve test instances, solver logs, and model documentation.
