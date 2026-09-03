# Phase 8 Implementation Prompt
# Baseline Agents and Environment Benchmarking

You are now implementing **Phase 8** of the project:

**"Emergent Cooperation in Multi-Agent Reinforcement Learning for Target Capture"**

You already have:

- Phase 0: repository foundation
- Phase 1: entity modeling
- Phase 2: GridWorld core
- Phase 3: agent movement mechanics
- Phase 4: target movement policy
- Phase 5: complete simulation environment
- Phase 6: target capture mechanism
- Phase 7: reward system

The current repository contains:

- TargetCaptureEnv
- GridWorld
- Agents
- Target
- MovementController
- CaptureChecker
- RewardCalculator

Your responsibility in this phase is ONLY to implement baseline agents for evaluating the environment.

---

# Important Scope Restriction

This phase is ONLY about baseline behavior.

Do NOT implement:

❌ reinforcement learning  
❌ Q-learning  
❌ neural networks  
❌ policy gradients  
❌ actor-critic  
❌ MARL algorithms  
❌ training loops  

Those belong to later phases.

---

# Phase 8 Objective

Create simple non-learning agents that allow us to benchmark the environment before introducing machine learning.

The project should support comparison between:

1. Random behavior
2. Simple heuristic behavior

These baselines will later be compared against learned agents.

---

# Scientific Motivation

Before claiming that reinforcement learning improves performance, we need to establish:

- how difficult the environment is
- how random behavior performs
- whether simple handcrafted strategies can solve the task

The baseline experiments should provide a reference point.

---

# Design Philosophy

## 1. Separate agents from environment

Agents should decide actions.

The environment should execute actions.

Do not put environment logic inside agents.

---

## 2. Common agent interface

Both baseline agents should follow a similar interface.

Example:

```python id="agentinterface"
class AgentPolicy:

    def select_action(self, observation):
        pass
```

The exact design may differ.

The important requirement:

Future RL agents should be replaceable without changing the environment.

---

# Required Files

Create:

```text id="baselinefiles"
agents/

├── __init__.py
├── random_agent.py
├── heuristic_agent.py
└── base_agent.py


experiments/

└── baseline_evaluation.py


tests/

└── test_baseline_agents.py
```

Modify existing files only if necessary.

---

# 1. Base Agent Interface

Create:

```text
agents/base_agent.py
```

Implement a simple interface.

Example:

```python
class BaseAgent:
    def select_action(self, observation):
        raise NotImplementedError
```

Purpose:

Provide a common structure.

Do not add unnecessary complexity.

---

# 2. Random Agent

Create:

```text
agents/random_agent.py
```

Implement:

```python
class RandomAgent(BaseAgent):
```

---

## Behavior

The RandomAgent selects actions randomly:

Available actions:

```text
UP
DOWN
LEFT
RIGHT
STAY
```

It does not consider:

- target position
- teammate position
- environment state

---

## Requirements

The agent should:

- use the existing Action enum
- support reproducibility with seed
- return valid actions only

Example:

```python
agent = RandomAgent(seed=42)

action = agent.select_action(observation)
```

---

# 3. Heuristic Agent

Create:

```text
agents/heuristic_agent.py
```

Implement:

```python
class HeuristicAgent(BaseAgent):
```

---

# Heuristic Strategy

The goal is not optimal behavior.

The goal is a simple intelligent baseline.

The agent should:

Move toward the target.

Use Manhattan distance.

Example:

Current:

```
Agent:
(2,2)

Target:
(5,2)
```

Preferred action:

```
RIGHT
```

---

# Heuristic Rules

Implement:

1. Calculate difference between agent and target.

Example:

```text
dx = target_x - agent_x
dy = target_y - agent_y
```

2. Choose movement that reduces distance.

Priority can be:

- horizontal movement
- vertical movement

or any documented deterministic strategy.

---

# Important Limitation

This heuristic agent is NOT cooperative.

It only tries to approach the target.

It does not intentionally coordinate with another agent.

This is useful because later MARL should outperform independent greedy behavior.

---

# Observation Format

For this phase, agents can receive the simple environment state.

Example:

```python
{
"agent_position": Position,
"target_position": Position
}
```

Do not create the final RL observation system yet.

---

# 4. Baseline Evaluation Script

Create:

```text
experiments/baseline_evaluation.py
```

Purpose:

Run baseline experiments.

---

The script should:

1. Create environment.
2. Initialize agents.
3. Run multiple episodes.
4. Collect metrics.

---

# Evaluation Metrics

Collect:

## Capture Rate

Formula:

```
successful episodes / total episodes
```

---

## Average Episode Length

Average number of steps per episode.

---

## Average Reward

Use Phase 7 reward calculator.

---

# Experiment Setup

Run at least:

```text
Random Agents
```

and:

```text
Heuristic Agents
```

---

Example:

```python
episodes = 100
```

The exact number can be configurable.

---

# Output Example

The script should produce something like:

```
Baseline Evaluation

Random Agent:
Capture Rate: 0.05
Average Steps: 95

Heuristic Agent:
Capture Rate: 0.40
Average Steps: 55
```

---

# Testing Requirements

Create:

```text
tests/test_baseline_agents.py
```

Use pytest.

---

# Test 1: Random Agent Output

Verify:

RandomAgent always returns:

```
Action enum values
```

---

# Test 2: Random Agent Reproducibility

Two agents:

```python
RandomAgent(seed=42)
```

should produce the same action sequence.

---

# Test 3: Heuristic Agent Direction

Scenario:

Agent:

```
(2,2)
```

Target:

```
(5,2)
```

Expected:

Action should move toward target.

---

# Test 4: Heuristic Distance Improvement

Verify:

After applying heuristic action:

distance should not increase.

---

# Test 5: Baseline Script Execution

Run a small experiment.

Verify:

- no crashes
- metrics are produced

---

# Documentation

Update README:

```markdown
## Current Implementation Status

Phase 8 completed:

Implemented:
- random baseline agent
- heuristic baseline agent
- baseline evaluation framework

Not implemented yet:
- reinforcement learning
- learned policies
- MARL algorithms
```

---

# Code Quality Requirements

Before finishing:

Check:

- baseline agents are independent from environment
- no RL code exists
- interfaces are reusable
- experiments are reproducible
- metrics are clearly defined

---

# Before Coding

Follow this workflow:

1. Inspect current repository.
2. Verify Phase 7 completion.
3. Explain planned changes.
4. Implement Phase 8 only.
5. Run tests.
6. Report results.

Do not expand scope.

---

# Definition of Done

Phase 8 is complete when:

✅ BaseAgent interface exists

✅ RandomAgent works

✅ HeuristicAgent works

✅ Baseline evaluation runs

✅ Capture rate is measured

✅ Average episode length is measured

✅ Tests pass

✅ Results are reproducible

✅ No RL algorithm exists

---

# Final Response Format

After implementation, provide:

## 1. Summary

What was implemented.

## 2. Files Created/Modified

List files.

## 3. Testing Results

Show pytest output.

## 4. Baseline Results

Report:

- Random performance
- Heuristic performance

## 5. Phase 9 Readiness

Explain why the project is ready for reinforcement learning implementation.

Do not implement Phase 9.