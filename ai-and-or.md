# AI and Operations Research

Resources and concepts at the intersection of artificial intelligence, machine learning, optimization, simulation, and decision science.

See also: [Methodologies](methodologies.md), [Learning Paths](learning-paths.md#data-scientist), [Papers](papers.md#or-and-machine-learning), [Libraries](libraries.md), and [Careers](careers.md#data-scientist-with-or-focus).

## Contents

- [Why AI and OR Belong Together](#why-ai-and-or-belong-together)
- [Reinforcement Learning](#reinforcement-learning)
- [Decision Intelligence](#decision-intelligence)
- [Neuro-Symbolic Optimization](#neuro-symbolic-optimization)
- [Learning-Augmented Optimization](#learning-augmented-optimization)
- [Digital Twins](#digital-twins)
- [Prescriptive Analytics](#prescriptive-analytics)
- [Optimization for Machine Learning](#optimization-for-machine-learning)
- [Machine Learning for Optimization](#machine-learning-for-optimization)
- [Tools and Libraries](#tools-and-libraries)
- [Papers and Surveys](#papers-and-surveys)

## Why AI and OR Belong Together

AI often predicts, classifies, recommends, or generates. OR decides under constraints, uncertainty, and tradeoffs. High-value systems increasingly combine both: prediction models estimate uncertain inputs, optimization models choose actions, simulation tests policies, and feedback loops update decisions over time.

## Reinforcement Learning

- Use when decisions are sequential, feedback is delayed, and exploration matters.
- OR connections: Markov decision processes, approximate dynamic programming, stochastic control, inventory control, fleet management, pricing, and resource allocation.
- Resources: [Stanford CS234](https://web.stanford.edu/class/cs234/), [Berkeley CS285](https://rail.eecs.berkeley.edu/deeprlcourse/), and [Bertsekas Dynamic Programming](https://web.mit.edu/dimitrib/www/dpbook.html).

## Decision Intelligence

- Focuses on the full decision pipeline: data, prediction, optimization, simulation, human judgment, deployment, monitoring, and governance.
- OR contribution: explicit objectives, constraints, sensitivity analysis, value of information, and robust decisions.
- Useful methods: decision analysis, influence diagrams, optimization models, simulation, causal inference, and scenario planning.

## Neuro-Symbolic Optimization

- Combines learned representations with symbolic constraints, search, logic, or mathematical programming.
- OR connections: constraint programming, mixed-integer programming, SAT/MaxSAT, planning, graph search, and decomposition.
- Example use cases: scheduling with learned priorities, routing with learned embeddings, and constrained generation.

## Learning-Augmented Optimization

- Uses predictions to improve algorithms while preserving worst-case guarantees or fallback behavior.
- OR connections: online algorithms, robust optimization, approximation algorithms, and algorithm configuration.
- Example use cases: caching, scheduling, inventory, matching, and resource allocation with demand forecasts.

## Digital Twins

- Digital twins combine simulation, real-time data, optimization, and visualization to test and control operational systems.
- OR contribution: optimization policies, simulation validation, experimental design, scenario analysis, and uncertainty quantification.
- Application areas: manufacturing, logistics, energy, healthcare, smart cities, and defense.

## Prescriptive Analytics

- Moves beyond descriptive and predictive analytics by recommending actions.
- OR methods: linear programming, MIP, stochastic programming, robust optimization, simulation optimization, and decision analysis.
- Typical workflow: forecast demand, optimize decisions, simulate outcomes, monitor results, and retrain models.

## Optimization for Machine Learning

- Optimization is the computational foundation of training, regularization, hyperparameter tuning, and constrained ML.
- Methods: gradient descent, stochastic gradient methods, convex optimization, proximal methods, Bayesian optimization, and constrained optimization.
- Tools: [SciPy Optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html), [CVXPY](https://www.cvxpy.org/), [PyTorch](https://pytorch.org/), [JAX](https://jax.readthedocs.io/), and [Optuna](https://optuna.org/).

## Machine Learning for Optimization

- ML can assist optimization by predicting good starts, branching decisions, cuts, primal heuristics, decomposition policies, or algorithm parameters.
- Methods: graph neural networks, imitation learning, reinforcement learning, algorithm selection, and learning-to-rank.
- Caution: evaluate decision quality, feasibility, robustness, and generalization across instances.

## Tools and Libraries

- [cvxpylayers](https://github.com/cvxgrp/cvxpylayers) - Differentiable convex optimization layers for PyTorch and JAX.
- [DiffOpt.jl](https://github.com/jump-dev/DiffOpt.jl) - Differentiable optimization through JuMP models.
- [PyEPO](https://github.com/khalil-research/PyEPO) - Predict-and-optimize library for decision-focused learning.
- [OR-Tools](https://developers.google.com/optimization) - Optimization tools useful for building decision systems.
- [Ray RLlib](https://docs.ray.io/en/latest/rllib/) - Reinforcement learning library for sequential decision experiments.
- [Optuna](https://optuna.org/) - Hyperparameter and black-box optimization framework.

## Papers and Surveys

- [Machine Learning for Combinatorial Optimization: A Methodological Tour d'Horizon](https://arxiv.org/abs/1811.06128) - Survey of ML for combinatorial optimization.
- [Decision-Focused Learning: Foundations, State of the Art, Benchmark and Future Opportunities](https://arxiv.org/abs/2307.13565) - Survey of decision-focused learning.
- [Smart Predict-then-Optimize](https://doi.org/10.1287/mnsc.2020.3922) - Decision-aware prediction framework.
- [Combinatorial Optimization with Graph Neural Networks](https://arxiv.org/abs/2102.09544) - Survey of GNN methods for combinatorial optimization.
- [Learning to Branch in Mixed Integer Programming](https://arxiv.org/abs/1803.03635) - Learning-based branching policies for MIP.
