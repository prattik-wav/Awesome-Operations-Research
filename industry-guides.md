# Operations Research by Industry

This file is a **practitioner- and career-oriented guide organized by industry**: for each sector it summarizes common problems, the methods and software used in practice, useful datasets, communities, and the roles to aim for. For a methods-and-problems overview of where OR is applied, see [Applications](applications.md).

See also: [Applications](applications.md), [Careers](careers.md), [Datasets](datasets.md), [Software](softwares.md), [Journals](journals.md), [Events](events.md), and [Learning Paths](learning-paths.md).

## Contents

- [Healthcare Operations Research](#healthcare-operations-research)
- [Supply Chain and Logistics](#supply-chain-and-logistics)
- [Transportation and Routing](#transportation-and-routing)
- [Airlines and Aviation](#airlines-and-aviation)
- [Manufacturing and Production](#manufacturing-and-production)
- [Energy Systems](#energy-systems)
- [Retail and E-Commerce](#retail-and-e-commerce)
- [Finance and Revenue Management](#finance-and-revenue-management)
- [Public Sector and Policy](#public-sector-and-policy)
- [Humanitarian Operations](#humanitarian-operations)
- [Defense and Military Operations](#defense-and-military-operations)
- [Telecommunications and Networks](#telecommunications-and-networks)
- [Smart Cities and Urban Systems](#smart-cities-and-urban-systems)

## Healthcare Operations Research

- Problems: appointment scheduling, patient flow, staffing, operating rooms, emergency departments, bed capacity, vaccination, screening, and resource allocation.
- Methods: queueing theory, simulation, integer programming, stochastic programming, Markov decision processes, and decision analysis.
- Software: [SimPy](libraries.md#python), [Arena](softwares.md#simulation-software), [AnyLogic](softwares.md#simulation-software), [Pyomo](libraries.md#python), [JuMP](libraries.md#julia), and [OR-Tools](softwares.md#open-source-solvers).
- Datasets: [MIMIC](datasets.md#healthcare-or-datasets), [PhysioNet](datasets.md#healthcare-or-datasets), [HealthData.gov](datasets.md#healthcare-or-datasets), and hospital operational data when available.
- Journals/conferences: [Operations Research](journals.md#flagship-or-journals), [MSOM](journals.md#flagship-or-journals), [INFORMS Healthcare](events.md#major-operations-research-and-management-science-conferences), and [ORAHS](events.md#major-operations-research-and-management-science-conferences).
- Courses/books: [Operations Research and Health Care](books.md#applied-or-and-analytics), [Simulation](books.md#simulation), and [Queueing Theory](books.md#queueing-theory).
- Careers: healthcare operations analyst, hospital analytics manager, simulation consultant, health policy modeler, and research scientist.

## Supply Chain and Logistics

- Problems: network design, procurement, S&OP, inventory, warehouse design, transportation planning, last-mile delivery, and resilience.
- Methods: LP, MIP, stochastic programming, robust optimization, facility location, routing, inventory theory, and simulation.
- Software: [Gurobi](softwares.md#commercial-solvers), [CPLEX](softwares.md#commercial-solvers), [Pyomo](libraries.md#python), [JuMP](libraries.md#julia), [OR-Tools](softwares.md#open-source-solvers), [AnyLogic](softwares.md#simulation-software), and [OpenSolver](softwares.md#spreadsheet-and-teaching-tools).
- Datasets: [OR-Library](datasets.md#optimization-benchmarks), [CVRPLIB](datasets.md#transportation-and-routing-datasets), [Amazon Last Mile](datasets.md#supply-chain-and-logistics-datasets), and public demand or logistics datasets.
- Journals/conferences: [MSOM](journals.md#flagship-or-journals), [EJOR](journals.md#applied-or-journals), [POMS](events.md#professional-societies), and [INFORMS Annual Meeting](events.md#major-operations-research-and-management-science-conferences).
- Courses/books: [Supply Chain and Inventory](courses.md#supply-chain-and-inventory), [Inventory and Supply Chain](books.md#inventory-and-supply-chain), and [Supply Chain Analyst](learning-paths.md#supply-chain-analyst).
- Careers: supply chain scientist, logistics analyst, network design analyst, inventory optimization analyst, and fulfillment optimization engineer.

## Transportation and Routing

- Problems: vehicle routing, transit planning, traffic assignment, fleet sizing, freight planning, mobility services, and port operations.
- Methods: shortest paths, min-cost flows, VRP heuristics, column generation, MIP, simulation, and stochastic models.
- Software: [OR-Tools Routing](tutorials.md#routing-tutorials), [Hexaly](solver-comparison.md#solver-notes), [Gurobi](solver-comparison.md#solver-notes), [SCIP](solver-comparison.md#solver-notes), [NetworkX](libraries.md#python), and GIS tools.
- Datasets: [CVRPLIB](datasets.md#transportation-and-routing-datasets), [TSPLIB](datasets.md#optimization-benchmarks), [Solomon VRPTW](datasets.md#transportation-and-routing-datasets), [OpenStreetMap](datasets.md#transportation-and-routing-datasets), and [TransportationNetworks](datasets.md#transportation-and-routing-datasets).
- Journals/conferences: [Transportation Science](journals.md#applied-or-journals), [Transportation Research Part B](journals.md#related-analytics-and-systems-journals), [TRISTAN](events.md#specialized-workshops), and [VeRoLog](events.md#specialized-workshops).
- Careers: transportation analyst, routing optimization engineer, mobility data scientist, logistics scientist, and network planning analyst.

## Airlines and Aviation

- Problems: fleet assignment, crew pairing, aircraft routing, maintenance planning, irregular operations, gate assignment, pricing, and revenue management.
- Methods: set partitioning, column generation, MIP, stochastic programming, dynamic programming, simulation, and robust optimization.
- Software: [Gurobi](softwares.md#commercial-solvers), [CPLEX](softwares.md#commercial-solvers), [FICO Xpress](softwares.md#commercial-solvers), [Pyomo](libraries.md#python), [JuMP](libraries.md#julia), and custom decomposition tools.
- Datasets: [Bureau of Transportation Statistics](https://www.transtats.bts.gov/), [OpenFlights](https://openflights.org/data.php), and public delay data.
- Journals/conferences: [Transportation Science](journals.md#applied-or-journals), [INFORMS Annual Meeting](events.md#major-operations-research-and-management-science-conferences), and [AGIFORS](https://agifors.org/).
- Careers: airline operations research analyst, revenue management analyst, crew scheduling analyst, network planning analyst, and operations control analyst.

## Manufacturing and Production

- Problems: production planning, lot sizing, scheduling, quality control, facility layout, workforce planning, maintenance, and digital twins.
- Methods: MIP, constraint programming, scheduling, simulation, inventory control, reliability models, and stochastic optimization.
- Software: [MiniZinc](softwares.md#constraint-programming-tools), [OR-Tools CP-SAT](softwares.md#constraint-programming-tools), [FlexSim](softwares.md#simulation-software), [Simio](softwares.md#simulation-software), [GAMS](softwares.md#modeling-languages-and-algebraic-modeling-systems), and [OpenSolver](softwares.md#spreadsheet-and-teaching-tools).
- Datasets: [PSPLIB](datasets.md#scheduling-benchmarks), [Taillard instances](datasets.md#scheduling-benchmarks), and OR-Library scheduling data.
- Journals/conferences: [IISE Transactions](journals.md#related-analytics-and-systems-journals), [MSOM](journals.md#flagship-or-journals), [POMS](events.md#professional-societies), and [Winter Simulation Conference](events.md#simulation-conferences).
- Careers: industrial engineer, manufacturing analytics engineer, production planning analyst, simulation engineer, and operations excellence consultant.

## Energy Systems

- Problems: unit commitment, economic dispatch, optimal power flow, capacity expansion, storage valuation, renewable integration, and market design.
- Methods: MIP, nonlinear programming, stochastic programming, robust optimization, decomposition, equilibrium modeling, and simulation.
- Software: [PowerModels.jl](libraries.md#julia), [MATPOWER](libraries.md#matlab), [Pyomo](libraries.md#python), [JuMP](libraries.md#julia), [Ipopt](softwares.md#open-source-solvers), [HiGHS](softwares.md#open-source-solvers), and [Gurobi](softwares.md#commercial-solvers).
- Datasets: [PGLib-OPF](datasets.md#energy-systems-optimization-datasets), [MATPOWER cases](datasets.md#energy-systems-optimization-datasets), [NREL Data Catalog](datasets.md#energy-systems-optimization-datasets), and IEEE test feeders.
- Journals/conferences: [EJOR](journals.md#applied-or-journals), [INFORMS](events.md#major-operations-research-and-management-science-conferences), [SIAM Optimization](events.md#optimization-and-mathematical-programming-conferences), and power systems venues.
- Careers: energy systems optimization analyst, power systems modeler, energy market analyst, grid analytics engineer, and DER optimization scientist.

## Retail and E-Commerce

- Problems: assortment, pricing, promotion planning, inventory, fulfillment, warehouse operations, ad allocation, and workforce scheduling.
- Methods: demand forecasting, revenue management, inventory theory, MIP, stochastic optimization, causal inference, simulation, and bandits.
- Software: [CVXPY](libraries.md#python), [Pyomo](libraries.md#python), [JuMP](libraries.md#julia), [Gurobi](softwares.md#commercial-solvers), [OR-Tools](softwares.md#open-source-solvers), and forecasting tools in Python/R.
- Datasets: [UCI Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail), public retail datasets, and demand datasets from [Kaggle](https://www.kaggle.com/datasets?search=retail).
- Journals/conferences: [MSOM](journals.md#flagship-or-journals), [Management Science](journals.md#flagship-or-journals), [POMS](events.md#professional-societies), and INFORMS analytics events.
- Careers: retail optimization analyst, pricing scientist, inventory scientist, marketplace optimization engineer, and demand planning analyst.

## Finance and Revenue Management

- Problems: portfolio optimization, risk management, asset-liability management, pricing, assortment, booking limits, and market-making.
- Methods: convex optimization, stochastic programming, robust optimization, dynamic programming, simulation, and multi-objective optimization.
- Software: [CVXPY](libraries.md#python), [MOSEK](softwares.md#commercial-solvers), [Gurobi](softwares.md#commercial-solvers), [JuMP](libraries.md#julia), [ROI](libraries.md#r), and Python/R analytics stacks.
- Datasets: [FRED](https://fred.stlouisfed.org/), public market data, synthetic portfolio instances, and licensed financial datasets.
- Journals/conferences: [Management Science](journals.md#flagship-or-journals), [Operations Research](journals.md#flagship-or-journals), and finance/analytics conferences.
- Careers: quantitative analyst, revenue management analyst, pricing scientist, risk optimization analyst, and portfolio optimization engineer.

## Public Sector and Policy

- Problems: emergency services, infrastructure planning, inspections, social program allocation, taxation, elections, fairness, and regulation.
- Methods: facility location, MIP, simulation, decision analysis, game theory, multi-objective optimization, and robust optimization.
- Software: [Pyomo](libraries.md#python), [JuMP](libraries.md#julia), [OpenSolver](softwares.md#spreadsheet-and-teaching-tools), simulation tools, GIS tools, and dashboards.
- Datasets: [data.gov](datasets.md#data-portals-useful-for-or), [World Bank Open Data](datasets.md#data-portals-useful-for-or), [Eurostat](datasets.md#data-portals-useful-for-or), and local open-data portals.
- Journals/conferences: [Decision Analysis](journals.md#flagship-or-journals), [JORS](journals.md#applied-or-journals), [INFORMS](events.md#major-operations-research-and-management-science-conferences), and public-sector OR communities.
- Careers: policy analyst, public-sector OR analyst, civic analytics scientist, emergency response modeler, and infrastructure planning analyst.

## Humanitarian Operations

- Problems: disaster response, relief distribution, evacuation, food aid, public health logistics, and resilience planning.
- Methods: facility location, vehicle routing, stochastic programming, robust optimization, simulation, and network resilience.
- Software: [OR-Tools](softwares.md#open-source-solvers), [Pyomo](libraries.md#python), [JuMP](libraries.md#julia), [AnyLogic](softwares.md#simulation-software), GIS tools, and open-data platforms.
- Datasets: disaster response datasets, open government data, transportation networks, population data, and humanitarian data portals.
- Journals/conferences: [INFORMS Doing Good with Good OR](competitions.md#industry-and-applied-or-challenges), [IFORS](events.md#professional-societies), and humanitarian logistics workshops.
- Careers: humanitarian logistics analyst, disaster response modeler, NGO analytics lead, public health operations analyst, and resilience planner.

## Defense and Military Operations

- Problems: logistics, readiness, maintenance, force structure, surveillance, wargaming, routing, and resource allocation.
- Methods: simulation, game theory, stochastic models, optimization under uncertainty, search theory, and multi-objective optimization.
- Software: simulation platforms, MIP solvers, network optimization tools, agent-based simulation, and decision analysis tools.
- Datasets: public defense research data, synthetic scenarios, logistics data, and geospatial data.
- Journals/conferences: [Military Operations Research Society](https://www.mors.org/), [Naval Research Logistics](journals.md#applied-or-journals), and [Winter Simulation Conference](events.md#simulation-conferences).
- Careers: defense OR analyst, wargaming analyst, logistics modeler, simulation engineer, and operations analyst.

## Telecommunications and Networks

- Problems: capacity planning, network design, routing, reliability, spectrum allocation, cloud resource allocation, and service operations.
- Methods: network optimization, queueing, stochastic processes, graph algorithms, facility location, and integer programming.
- Software: [NetworkX](libraries.md#python), [Graphs.jl](libraries.md#julia), [JGraphT](libraries.md#java), [Gurobi](softwares.md#commercial-solvers), [HiGHS](softwares.md#open-source-solvers), and simulation tools.
- Datasets: [CAIDA datasets](https://www.caida.org/catalog/datasets/), public network topologies, synthetic traffic matrices, and telecom regulatory data.
- Journals/conferences: queueing and network venues, [SIAM](events.md#professional-societies), and IEEE communications communities.
- Careers: network optimization engineer, telecom analytics scientist, capacity planning analyst, cloud optimization engineer, and reliability modeler.

## Smart Cities and Urban Systems

- Problems: traffic, public transit, emergency services, waste collection, energy, water, parking, land use, and urban resilience.
- Methods: network optimization, simulation, facility location, multi-objective optimization, robust optimization, queueing, and digital twins.
- Software: [SUMO](https://www.eclipse.org/sumo/), [AnyLogic](softwares.md#simulation-software), [OpenStreetMap](datasets.md#transportation-and-routing-datasets), [OR-Tools](softwares.md#open-source-solvers), [Pyomo](libraries.md#python), and [JuMP](libraries.md#julia).
- Datasets: [OpenStreetMap](datasets.md#transportation-and-routing-datasets), [data.gov](datasets.md#data-portals-useful-for-or), local open-data portals, GTFS feeds, and mobility datasets.
- Journals/conferences: [Transportation Science](journals.md#applied-or-journals), [Transportation Research Part B](journals.md#related-analytics-and-systems-journals), and smart-city research venues.
- Careers: urban analytics scientist, transportation modeler, civic technology analyst, digital twin engineer, and infrastructure optimization analyst.
