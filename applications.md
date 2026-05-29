# Applications of Operations Research

Operations Research is a field of modeling and decision-making, not just a collection of algorithms. This file focuses on **where OR is applied and what problems OR solves** in each domain, with representative methods, software, datasets, and reading paths. For a practitioner- and career-oriented view organized by industry, see [Industry Guides](industry-guides.md).

See also: [Industry Guides](industry-guides.md), [Careers](careers.md), [Case Studies](case-studies.md), [Datasets](datasets.md), [Software](softwares.md), and [Methodologies](methodologies.md).

## Contents

- [Supply Chain and Logistics](#supply-chain-and-logistics)
- [Airlines](#airlines)
- [Transportation and Routing](#transportation-and-routing)
- [Healthcare Operations](#healthcare-operations)
- [Manufacturing and Production](#manufacturing-and-production)
- [Retail](#retail)
- [Energy Systems](#energy-systems)
- [Finance and Revenue Management](#finance-and-revenue-management)
- [Public Sector and Policy](#public-sector-and-policy)
- [Humanitarian Operations](#humanitarian-operations)
- [Military and Defense](#military-and-defense)
- [Telecommunications](#telecommunications)
- [Smart Cities](#smart-cities)
- [Sports Analytics](#sports-analytics)
- [Education and Workforce Planning](#education-and-workforce-planning)

## Supply Chain and Logistics

OR supports network design, facility location, inventory control, procurement, production-distribution planning, warehouse design, and resilience planning.

- Common methods: linear programming, mixed-integer programming, stochastic programming, robust optimization, simulation, inventory theory, and decomposition.
- Useful tools: [Pyomo](https://www.pyomo.org/), [JuMP](https://jump.dev/), [Gurobi](https://www.gurobi.com/), [IBM CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio), [AnyLogic](https://www.anylogic.com/), and [SimPy](https://simpy.readthedocs.io/).
- Useful benchmarks: [OR-Library](http://people.brunel.ac.uk/~mastjjb/jeb/info.html), [MIPLIB](https://miplib.zib.de/), and public supply chain datasets listed in [datasets.md](datasets.md).
- References: [MIT CTL](https://ctl.mit.edu/), [Supply Chain Management](https://www.pearson.com/en-us/subject-catalog/p/supply-chain-management-strategy-planning-and-operation/P200000003508), and [Designing and Managing the Supply Chain](https://www.mheducation.com/highered/product/designing-managing-supply-chain-simchi-levi-kaminsky/M9780073341521.html).

## Airlines

Airline OR is one of the classic success stories of large-scale optimization, combining scheduling, revenue management, fleet planning, crew pairing, maintenance, disruption recovery, and passenger flow.

- Common methods: set partitioning, column generation, integer programming, stochastic programming, dynamic programming, simulation, and robust optimization.
- Useful tools: [Gurobi](https://www.gurobi.com/), [IBM CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio), [FICO Xpress](https://www.fico.com/en/products/fico-xpress-optimization), [Pyomo](https://www.pyomo.org/), [JuMP](https://jump.dev/), and [OR-Tools](https://developers.google.com/optimization).
- Useful datasets: [Bureau of Transportation Statistics](https://www.transtats.bts.gov/), [OpenFlights](https://openflights.org/data.html), and airline delay datasets on [data.gov](https://www.data.gov/).
- References: [Transportation Science](https://pubsonline.informs.org/journal/trsc), [Revenue Management and Pricing](https://link.springer.com/book/10.1007/978-0-387-36064-7), and airline Edelman award papers in INFORMS publications.

## Transportation and Routing

OR is central to routing, fleet assignment, transit planning, traffic assignment, crew pairing, airline scheduling, port operations, and last-mile delivery.

- Common methods: shortest path, min-cost flow, vehicle routing heuristics, column generation, set partitioning, simulation, and stochastic models.
- Useful tools: [OR-Tools Routing](https://developers.google.com/optimization/routing), [Hexaly](https://www.hexaly.com/), [Gurobi](https://www.gurobi.com/), [SCIP](https://www.scipopt.org/), and GIS tooling built around [OpenStreetMap](https://www.openstreetmap.org/).
- Useful benchmarks: [CVRPLIB](http://vrp.galgos.inf.puc-rio.br/index.php/en/), [TSPLIB](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/), [Solomon VRPTW](https://www.sintef.no/projectweb/top/vrptw/solomon-benchmark/), and [TransportationNetworks](https://github.com/bstabler/TransportationNetworks).
- References: [Transportation Science](https://pubsonline.informs.org/journal/trsc), [Transportation Research Part B](https://www.sciencedirect.com/journal/transportation-research-part-b-methodological), and [Vehicle Routing](https://epubs.siam.org/doi/book/10.1137/1.9781611973594).

## Healthcare Operations

Healthcare OR improves access, quality, cost, and resilience in hospitals, clinics, emergency care, public health, and health policy.

- Common methods: queueing, simulation, appointment scheduling, staffing optimization, Markov decision processes, resource allocation, and stochastic programming.
- Useful tools: [SimPy](https://simpy.readthedocs.io/), [Arena](https://www.rockwellautomation.com/en-us/products/software/arena-simulation.html), [AnyLogic](https://www.anylogic.com/), [Pyomo](https://www.pyomo.org/), and [OR-Tools](https://developers.google.com/optimization).
- Useful resources: [ORAHS](https://orahs.di.unito.it/), [INFORMS Healthcare](https://www.informs.org/Community/Healthcare), [PhysioNet](https://physionet.org/), and [HealthData.gov](https://healthdata.gov/).
- References: [Operations Research and Health Care](https://link.springer.com/book/10.1007/978-1-4615-0807-3), [INFORMS Healthcare Conference](https://www.informs.org/Meetings-Conferences), and [MIMIC](https://physionet.org/content/mimiciv/).

## Manufacturing and Production

OR is used for production planning, lot sizing, machine scheduling, maintenance planning, quality control, facility layout, and digital twin simulation.

- Common methods: MIP, constraint programming, scheduling theory, discrete-event simulation, inventory control, and reliability models.
- Useful tools: [CP-SAT](https://developers.google.com/optimization/cp/cp_solver), [MiniZinc](https://www.minizinc.org/), [FlexSim](https://www.flexsim.com/), [Simio](https://www.simio.com/), [OpenSolver](https://opensolver.org/), and [GAMS](https://www.gams.com/).
- Useful benchmarks: [PSPLIB](https://www.om-db.wi.tum.de/psplib/), [Taillard scheduling instances](http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html), and OR-Library scheduling data.
- References: [Scheduling: Theory, Algorithms, and Systems](https://link.springer.com/book/10.1007/978-3-319-26580-3), [Winter Simulation Conference](https://meetings.informs.org/wordpress/wsc/), and [IISE](https://www.iise.org/).

## Retail

Retail OR improves pricing, promotion planning, assortment, inventory, shelf-space allocation, fulfillment, workforce scheduling, and omnichannel operations.

- Common methods: demand forecasting, assortment optimization, revenue management, inventory theory, stochastic programming, MIP, causal inference, and simulation.
- Useful tools: [CVXPY](https://www.cvxpy.org/), [Pyomo](https://www.pyomo.org/), [JuMP](https://jump.dev/), [Gurobi](https://www.gurobi.com/), [OR-Tools](https://developers.google.com/optimization), and forecasting tools in Python or R.
- Useful datasets: [Kaggle retail datasets](https://www.kaggle.com/datasets?search=retail), [UCI Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail), and public transaction or demand datasets from open-data portals.
- References: [Manufacturing & Service Operations Management](https://pubsonline.informs.org/journal/msom), [Production and Operations Management](https://onlinelibrary.wiley.com/journal/19375956), and [Revenue Management and Pricing](https://link.springer.com/book/10.1007/978-0-387-36064-7).

## Energy Systems

Energy OR supports power system planning, unit commitment, economic dispatch, optimal power flow, renewable integration, storage valuation, and market design.

- Common methods: mixed-integer programming, nonlinear programming, stochastic programming, robust optimization, decomposition, and equilibrium modeling.
- Useful tools: [PowerModels.jl](https://lanl-ansi.github.io/PowerModels.jl/stable/), [MATPOWER](https://matpower.org/), [Pyomo](https://www.pyomo.org/), [JuMP](https://jump.dev/), [Ipopt](https://coin-or.github.io/Ipopt/), and [HiGHS](https://highs.dev/).
- Useful benchmarks: [PGLib-OPF](https://github.com/power-grid-lib/pglib-opf), [MATPOWER cases](https://matpower.org/), [NREL Data Catalog](https://data.nrel.gov/), and IEEE test feeders.
- References: [Power Grid Lib](https://github.com/power-grid-lib), [NREL REopt](https://reopt.nrel.gov/), and energy optimization papers in [Optimization Online](https://optimization-online.org/).

## Finance and Revenue Management

OR supports portfolio construction, asset-liability management, risk controls, pricing, assortment, booking limits, market making, and revenue optimization.

- Common methods: convex optimization, stochastic programming, robust optimization, dynamic programming, simulation, and multi-objective optimization.
- Useful tools: [CVXPY](https://www.cvxpy.org/), [MOSEK](https://www.mosek.com/), [Gurobi](https://www.gurobi.com/), [R ROI](https://roi.r-forge.r-project.org/), and [Julia JuMP](https://jump.dev/).
- Useful reading: [Revenue Management and Pricing](https://link.springer.com/book/10.1007/978-0-387-36064-7), [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/), and robust optimization references in [books.md](books.md).
- Useful datasets: market data from regulated sources, synthetic portfolio data, [FRED](https://fred.stlouisfed.org/), and carefully licensed vendor datasets.

## Public Sector and Policy

Governments and public agencies use OR for infrastructure planning, emergency services, social programs, elections, tax compliance, inspection, and resource allocation.

- Common methods: facility location, integer programming, simulation, decision analysis, game theory, multi-criteria decision analysis, and fairness-aware optimization.
- Useful datasets: [data.gov](https://www.data.gov/), [World Bank Open Data](https://data.worldbank.org/), [Eurostat](https://ec.europa.eu/eurostat), and local open-data portals.
- Useful communities: [INFORMS Public Sector OR](https://www.informs.org/Community), [The OR Society](https://www.theorsociety.com/), and [IFORS](https://ifors.org/).

## Humanitarian Operations

Humanitarian OR supports disaster response, relief distribution, emergency facility placement, evacuation planning, food systems, and public health logistics.

- Common methods: stochastic programming, robust optimization, vehicle routing, facility location, simulation, and network interdiction/resilience models.
- Useful resources: [IFORS](https://ifors.org/), [INFORMS Doing Good with Good OR](https://www.informs.org/Recognizing-Excellence/INFORMS-Prizes/Doing-Good-with-Good-OR), and public disaster response datasets from government portals.

## Military and Defense

Defense OR covers logistics, wargaming, readiness, maintenance, force structure, surveillance, resource allocation, and operational planning.

- Common methods: simulation, game theory, stochastic models, optimization under uncertainty, search theory, and multi-objective optimization.
- Useful resources: [Military Operations Research Society](https://www.mors.org/), [INFORMS](https://www.informs.org/), and public defense research repositories.
- Useful tools: simulation platforms, agent-based simulation, MIP solvers, network optimization tools, and decision analysis frameworks.
- References: [Naval Research Logistics](https://onlinelibrary.wiley.com/journal/15206750), [MORS](https://www.mors.org/), and [Winter Simulation Conference](https://meetings.informs.org/wordpress/wsc/).

## Telecommunications

Telecommunications OR focuses on network design, capacity planning, routing, reliability, spectrum allocation, and service operations.

- Common methods: network optimization, queueing, stochastic processes, graph algorithms, facility location, and integer programming.
- Useful tools: graph libraries, [NetworkX](https://networkx.org/), [Graphs.jl](https://juliagraphs.org/Graphs.jl/stable/), [Gurobi](https://www.gurobi.com/), and [HiGHS](https://highs.dev/).
- Useful datasets: public network topologies, synthetic traffic matrices, [CAIDA datasets](https://www.caida.org/catalog/datasets/), and telecommunications regulatory data.
- References: queueing texts in [books.md](books.md), network optimization benchmarks in [datasets.md](datasets.md), and [IEEE communications venues](https://www.comsoc.org/).

## Smart Cities

Smart-city OR combines transportation, energy, water, waste, emergency response, land use, public safety, and digital infrastructure decisions.

- Common methods: network optimization, simulation, facility location, multi-objective optimization, robust optimization, queueing, and digital twins.
- Useful tools: [AnyLogic](https://www.anylogic.com/), [SUMO](https://www.eclipse.org/sumo/), [OpenStreetMap](https://www.openstreetmap.org/), [OR-Tools](https://developers.google.com/optimization), [Pyomo](https://www.pyomo.org/), and [JuMP](https://jump.dev/).
- Useful datasets: [OpenStreetMap](https://www.openstreetmap.org/), [data.gov](https://www.data.gov/), [Eurostat](https://ec.europa.eu/eurostat), local open-data portals, and public transit GTFS feeds.
- References: transportation journals in [journals.md](journals.md), urban analytics courses, and smart infrastructure research centers.

## Sports Analytics

Sports OR supports scheduling, tournament design, player evaluation, lineup optimization, travel planning, and officiating assignments.

- Common methods: integer programming, matching, ranking models, simulation, stochastic dynamic programming, and multi-objective optimization.
- Useful tools: [OR-Tools](https://developers.google.com/optimization), [Pyomo](https://www.pyomo.org/), [JuMP](https://jump.dev/), and statistical modeling tools in Python or R.

## Education and Workforce Planning

Education systems and employers use OR for timetabling, course assignment, staff scheduling, capacity planning, admissions operations, and workforce rostering.

- Common methods: constraint programming, mixed-integer programming, matching, simulation, and queueing.
- Useful tools: [Timefold Solver](https://timefold.ai/), [OR-Tools CP-SAT](https://developers.google.com/optimization/cp/cp_solver), [MiniZinc](https://www.minizinc.org/), [Choco Solver](https://choco-solver.org/), and [OptaPlanner](https://www.optaplanner.org/).
