# Operations Research Case Studies

Landmark and teaching-oriented case studies showing how Operations Research methods create value in practice. Some cases involve proprietary systems, so descriptions are intentionally careful and source-oriented.

See also: [Applications](applications.md), [Industry Guides](industry-guides.md), [Teaching](teaching.md), [Papers](papers.md), [Events](events.md), and [INFORMS Edelman Award](https://www.informs.org/Recognizing-Excellence/INFORMS-Prizes/Franz-Edelman-Award).

## Contents

- [Airline Scheduling and Revenue Management](#airline-scheduling-and-revenue-management)
- [UPS Routing and Logistics](#ups-routing-and-logistics)
- [Amazon Fulfillment and Supply Chain](#amazon-fulfillment-and-supply-chain)
- [Military and Defense Logistics](#military-and-defense-logistics)
- [Healthcare Capacity Planning](#healthcare-capacity-planning)
- [Sports Scheduling](#sports-scheduling)
- [Energy Grid Optimization](#energy-grid-optimization)
- [Disaster Response and Humanitarian Logistics](#disaster-response-and-humanitarian-logistics)
- [Manufacturing Production Planning](#manufacturing-production-planning)
- [Public Sector Resource Allocation](#public-sector-resource-allocation)

## Airline Scheduling and Revenue Management

- Problem context: Airlines must coordinate fleet assignment, crew pairing, aircraft routing, maintenance, pricing, overbooking, and disruption recovery.
- OR methods used: set partitioning, column generation, integer programming, dynamic programming, stochastic programming, and simulation.
- Outcome or value created: Airline OR is widely reported as one of the highest-impact application areas for large-scale optimization and revenue management.
- Related resources: [Airlines and Aviation](industry-guides.md#airlines-and-aviation), [Revenue Management](careers.md#revenue-management-analyst), [Transportation Science](journals.md#applied-or-journals), and [Vehicle Routing and Logistics](methodologies.md#vehicle-routing-and-logistics).
- References: [AGIFORS](https://agifors.org/), [INFORMS Edelman Award](https://www.informs.org/Recognizing-Excellence/INFORMS-Prizes/Franz-Edelman-Award), and [Revenue Management and Pricing](books.md#applied-or-and-analytics).

## UPS Routing and Logistics

- Problem context: Parcel carriers must route drivers, sequence deliveries, manage pickup commitments, and adapt to large daily demand fluctuations.
- OR methods used: vehicle routing, network optimization, heuristics, geospatial analytics, telematics, and large-scale decision support.
- Outcome or value created: UPS ORION is widely cited as a major industrial routing optimization system.
- Related resources: [Transportation and Routing](industry-guides.md#transportation-and-routing), [Vehicle Routing and Logistics](methodologies.md#vehicle-routing-and-logistics), [CVRPLIB](datasets.md#transportation-and-routing-datasets), and [OR-Tools Routing](tutorials.md#routing-tutorials).
- References: [INFORMS Edelman Award](https://www.informs.org/Recognizing-Excellence/INFORMS-Prizes/Franz-Edelman-Award), [Transportation Science](journals.md#applied-or-journals), and UPS ORION public talks and articles.

## Amazon Fulfillment and Supply Chain

- Problem context: E-commerce fulfillment requires inventory placement, warehouse operations, labor planning, routing, delivery promises, and marketplace decisions.
- OR methods used: network design, MIP, stochastic optimization, simulation, queueing, routing, forecasting, and ML-assisted optimization.
- Outcome or value created: Amazon publicly describes extensive use of OR and optimization in fulfillment, delivery, and operations.
- Related resources: [Amazon Science OR and Optimization](blogs.md#analytics-and-decision-science-blogs), [Supply Chain and Logistics](industry-guides.md#supply-chain-and-logistics), [Retail and E-Commerce](industry-guides.md#retail-and-e-commerce), and [Amazon Last Mile](datasets.md#supply-chain-and-logistics-datasets).
- References: [Amazon Science](https://www.amazon.science/research-areas/operations-research-and-optimization), [MIPLIB](datasets.md#optimization-benchmarks), and [CVRPLIB](datasets.md#transportation-and-routing-datasets).

## Military and Defense Logistics

- Problem context: Defense organizations plan transportation, maintenance, readiness, inventory, search, surveillance, and deployment under uncertainty.
- OR methods used: simulation, stochastic models, game theory, network optimization, search theory, and robust optimization.
- Outcome or value created: Military needs were central to the historical development of OR and remain a major application area.
- Related resources: [Defense and Military Operations](industry-guides.md#defense-and-military-operations), [Operations Research History](history.md), [Simulation](methodologies.md#simulation), and [Robust Optimization](methodologies.md#robust-optimization).
- References: [Military Operations Research Society](https://www.mors.org/), [Naval Research Logistics](journals.md#applied-or-journals), and [Winter Simulation Conference](events.md#simulation-conferences).

## Healthcare Capacity Planning

- Problem context: Hospitals and health systems must plan beds, staffing, appointments, operating rooms, emergency departments, and patient flow.
- OR methods used: queueing, discrete-event simulation, scheduling, MIP, Markov decision processes, and stochastic programming.
- Outcome or value created: Healthcare OR is commonly used to reveal bottlenecks, evaluate capacity policies, and improve access under uncertainty.
- Related resources: [Healthcare Operations Research](industry-guides.md#healthcare-operations-research), [Healthcare Operations Analyst](careers.md#healthcare-operations-analyst), [Simulation](methodologies.md#simulation), and [Queueing Theory](methodologies.md#queueing-theory).
- References: [ORAHS](events.md#major-operations-research-and-management-science-conferences), [Operations Research and Health Care](books.md#applied-or-and-analytics), and [HealthData.gov](datasets.md#healthcare-or-datasets).

## Sports Scheduling

- Problem context: Leagues must create schedules satisfying venue, travel, rest, broadcast, rivalry, fairness, and competitive constraints.
- OR methods used: integer programming, constraint programming, local search, decomposition, and heuristics.
- Outcome or value created: Sports scheduling is a widely used teaching example because constraints are understandable but computationally rich.
- Related resources: [Scheduling](methodologies.md#scheduling), [Sports Analytics](applications.md#sports-analytics), [Michael Trick](researchers.md#scheduling), and [OR-Tools Scheduling](tutorials.md#scheduling-tutorials).
- References: [Michael Trick's Operations Research Blog](blogs.md#operations-research-blogs), [Scheduling books](books.md#scheduling), and [CPAIOR](events.md#optimization-and-mathematical-programming-conferences).

## Energy Grid Optimization

- Problem context: Grid operators and energy planners solve dispatch, unit commitment, capacity expansion, storage, renewable integration, and market-clearing problems.
- OR methods used: LP, MIP, nonlinear programming, stochastic programming, robust optimization, decomposition, and equilibrium models.
- Outcome or value created: OR methods are fundamental to reliable, cost-effective, and increasingly low-carbon power system operation.
- Related resources: [Energy Systems](industry-guides.md#energy-systems), [Energy datasets](datasets.md#energy-systems-optimization-datasets), [PowerModels.jl](libraries.md#julia), and [Solver Comparison](solver-comparison.md).
- References: [PGLib-OPF](datasets.md#energy-systems-optimization-datasets), [MATPOWER](datasets.md#energy-systems-optimization-datasets), and [NREL Data Catalog](datasets.md#energy-systems-optimization-datasets).

## Disaster Response and Humanitarian Logistics

- Problem context: Disaster response requires pre-positioning supplies, routing relief, allocating scarce resources, and planning under damaged infrastructure.
- OR methods used: facility location, vehicle routing, stochastic programming, robust optimization, simulation, and network resilience.
- Outcome or value created: OR provides transparent planning tools for preparedness, response, and recovery decisions.
- Related resources: [Humanitarian Operations](industry-guides.md#humanitarian-operations), [Facility Location](methodologies.md#facility-location), [Robust Optimization](methodologies.md#robust-optimization), and [Public Sector and Policy](industry-guides.md#public-sector-and-policy).
- References: [INFORMS Doing Good with Good OR](competitions.md#industry-and-applied-or-challenges), [IFORS](events.md#professional-societies), and public open-data portals.

## Manufacturing Production Planning

- Problem context: Manufacturers coordinate materials, machines, labor, maintenance, quality, and production schedules.
- OR methods used: MIP, lot sizing, scheduling, constraint programming, simulation, inventory theory, and reliability modeling.
- Outcome or value created: Production planning is a core teaching and practice area where optimization and simulation are often combined.
- Related resources: [Manufacturing and Production](industry-guides.md#manufacturing-and-production), [Scheduling](methodologies.md#scheduling), [Inventory Theory](methodologies.md#inventory-theory), and [Teaching](teaching.md).
- References: [PSPLIB](datasets.md#scheduling-benchmarks), [Taillard scheduling instances](datasets.md#scheduling-benchmarks), and [IISE](events.md#professional-societies).

## Public Sector Resource Allocation

- Problem context: Public agencies allocate emergency services, inspections, infrastructure, budgets, staff, and social services under fairness and transparency constraints.
- OR methods used: facility location, MIP, simulation, decision analysis, multi-objective optimization, and robust optimization.
- Outcome or value created: OR can help agencies compare tradeoffs, document assumptions, and improve resource allocation.
- Related resources: [Public Sector and Policy](industry-guides.md#public-sector-and-policy), [Decision Analysis](methodologies.md#decision-analysis), [Smart Cities](industry-guides.md#smart-cities-and-urban-systems), and [Careers](careers.md).
- References: [Decision Analysis](journals.md#flagship-or-journals), [data.gov](datasets.md#data-portals-useful-for-or), and [World Bank Open Data](datasets.md#data-portals-useful-for-or).
