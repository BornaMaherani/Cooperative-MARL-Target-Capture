# Emergent Cooperation in Multi-Agent Reinforcement Learning for Target Capture

This project studies cooperative behavior in multi-agent reinforcement learning.
Multiple agents learn to capture a moving target.
The goal is to investigate the emergence of cooperation.

## Current Implementation Status

Phase 10 completed:

Implemented:
- shared-policy cooperative Q-learning baseline
- agent-centric relative state representation
- shared Q-table parameters
- teammate-aware cooperative exploration
- independent and cooperative evaluation frameworks

Not implemented yet:
- sophisticated deep MARL
- learned multi-agent communication
- continuous action spaces

## Shared-Policy Cooperative Q-Learning

To introduce explicit cooperative learning while keeping the algorithm interpretable, both homogeneous hunter agents share a single tabular Q-function.

Each hunter acts from an agent-centric state containing:
- relative target position
- relative teammate position

Experience from both hunters updates the same Q-table. This experiment evaluates whether parameter sharing and teammate-aware state representations improve coordination compared with Independent Q-Learning.

## Experiments

### Experimental Setup
We conducted a rigorous academic evaluation of all four baseline methods. For learning algorithms, we trained independent models across **5 distinct seeds** for **5000 episodes** each. All models (and non-learning baselines) were then evaluated across **500 episodes per seed** with exploration strictly disabled (`epsilon = 0`).

### Quantitative Results
*mean ± standard deviation across 5 independent seeds*

| Method | Capture Rate | Capture Time | Episode Reward |
|--------|--------------|--------------|----------------|
| **Random** | 0.07 ± 0.01 | 43.89 ± 9.13 | -2.76 ± 0.33 |
| **Heuristic** | 0.35 ± 0.00 | 7.33 ± 0.29 | 13.63 ± 0.12 |
| **Independent Q-Learning** | 0.99 ± 0.00 | 20.49 ± 0.38 | 30.07 ± 0.09 |
| **Cooperative Q-Learning** | **1.00 ± 0.00** | **16.75 ± 0.85** | **30.28 ± 0.07** |

### Key Observations
1. **Learning vastly outperforms heuristics**: Both reinforcement learning methods learned to capture the target consistently (~100% capture rate), whereas the greedy Heuristic agent often got stuck or failed to corner the target within the time limit.
2. **Cooperation improves efficiency**: Shared-Policy Cooperative Q-Learning was able to capture the target significantly faster (mean 16.75 steps) than Independent Q-Learning (mean 20.49 steps).
3. **Parameter sharing stabilizes learning**: The standard deviations across seeds were consistently small for both learning methods, but the shared-policy method achieved a flawless 1.0 capture rate across all evaluation seeds.

### Limitations
- **Small GridWorld**: Evaluated on a 10x10 GridWorld; tabular methods will struggle to scale to much larger environments.
- **Tabular State Representation**: The relative coordinate space is compact, but it cannot generalize to unseen geometric scenarios without function approximation.
- **Homogeneity Required**: Parameter sharing inherently assumes symmetric capabilities, which would not apply to heterogeneous agent teams.

## Future Roadmap

Phase 0:
Project initialization

Phase 1:
GridWorld environment

Phase 2:
Environment mechanics

Phase 3:
Baseline agents

Phase 4:
Reinforcement learning

Phase 5:
Cooperative learning experiments

Phase 6:
Analysis and documentation

## Installation

```bash
git clone <repository-url>
cd Cooperative-MARL-Target-Capture
pip install -r requirements.txt
```
