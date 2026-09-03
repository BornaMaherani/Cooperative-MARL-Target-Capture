# Phase 7 Implementation Prompt
# Reward System and Reward Calculation Module

You are now implementing **Phase 7** of the project:

**"Emergent Cooperation in Multi-Agent Reinforcement Learning for Target Capture"**

You already have:

- Phase 0: repository foundation
- Phase 1: entity modeling
- Phase 2: GridWorld core
- Phase 3: agent movement mechanics
- Phase 4: target movement policy
- Phase 5: complete simulation environment
- Phase 6: target capture mechanism

The repository currently contains:

- Position
- Agent
- Target
- GridWorld
- MovementController
- TargetPolicy
- TargetCaptureEnv
- CaptureChecker

Your responsibility in this phase is ONLY to design and implement the reward system.

---

# Important Scope Restriction

This phase is ONLY about reward calculation.

Do NOT implement:

❌ reinforcement learning algorithms  
❌ Q-learning  
❌ neural networks  
❌ training loops  
❌ replay buffers  
❌ policies  
❌ optimization  
❌ experiment runners  

Those belong to later phases.

---

# Phase 7 Objective

Create a modular reward system that measures the quality of agent behavior.

The reward should encourage:

1. Moving closer to the target.
2. Successful cooperative capture.
3. Faster completion of the task.

The reward system must be:

- understandable
- configurable
- testable
- independent from learning algorithms

---

# Reward Design

Implement the following reward components:

\[
R_{total}
=
w_1 R_{distance}
+
w_2 R_{capture}
+
w_3 R_{step}
\]

where:

- R_distance = distance improvement reward
- R_capture = team capture reward
- R_step = time penalty

---

# Design Philosophy

## 1. Reward is separate from Environment

Do not put reward formulas directly inside:

- Agent
- Target
- GridWorld

Create a separate reward module.

Recommended:

```text id="reward1"
env/

├── rewards.py
```

---

# 2. Reward Calculator

Create:

```text id="reward2"
env/rewards.py
```

Implement:

```python id="reward3"
class RewardCalculator:
```

The exact name can differ if a better design exists.

---

# Constructor

The reward calculator should accept configurable weights.

Example:

```python
RewardCalculator(
    distance_weight=1.0,
    capture_weight=20.0,
    step_penalty=-0.05
)
```

Do not hard-code values inside methods.

---

# Reward Components

## 1. Distance Reward

Implement:

```python
calculate_distance_reward()
```

Purpose:

Reward agents when they reduce distance to the target.

Formula:

\[
R_{distance}=d_{previous}-d_{current}
\]

where:

```text
d = Manhattan distance
```

Example:

Previous:

```
distance = 6
```

Current:

```
distance = 4
```

Reward:

```
+2
```

---

If agents move farther:

Example:

Previous:

```
distance = 3
```

Current:

```
distance = 5
```

Reward:

```
-2
```

---

# 2. Capture Reward

Implement:

```python
calculate_capture_reward()
```

When:

```python
captured == True
```

Return:

```
+20
```

Otherwise:

```
0
```

The reward should represent team success.

All agents should conceptually receive the same capture reward.

---

# 3. Step Penalty

Implement:

```python
calculate_step_penalty()
```

Every timestep:

Return:

```
-0.05
```

Purpose:

Encourage faster capture.

---

# 4. Total Reward

Implement:

```python
calculate_total_reward()
```

Combine:

```
distance_reward
+
capture_reward
+
step_penalty
```

with weights.

Example:

```python
total =
w1 * distance_reward
+
w2 * capture_reward
+
w3 * step_penalty
```

---

# Reward API Design

The final API should be clean.

Example:

```python
reward_calculator.calculate(
    agents=agents,
    target=target,
    previous_positions=previous_positions,
    captured=captured
)
```

Return:

A dictionary:

```python
{
    "distance_reward": 1.5,
    "capture_reward": 0,
    "step_penalty": -0.05,
    "total_reward": 1.45
}
```

This makes debugging easier.

---

# Integration With Environment

Modify:

```text
env/target_capture_env.py
```

ONLY if necessary.

Do NOT make the environment dependent on reward yet.

The environment can optionally expose reward calculation support.

The goal is:

Future RL phases can easily call:

```python
reward = reward_calculator.calculate(...)
```

---

# Important Design Rule

Reward calculation should be a pure operation.

Given the same input:

same output.

Avoid:

- hidden state
- randomness
- external dependencies

---

# Testing Requirements

Create:

```text
tests/test_rewards.py
```

Use pytest.

---

# Test 1: Distance Reward Positive

Scenario:

Previous distance:

```
10
```

Current distance:

```
6
```

Expected:

Positive reward.

---

# Test 2: Distance Reward Negative

Scenario:

Previous distance:

```
5
```

Current distance:

```
8
```

Expected:

Negative reward.

---

# Test 3: Capture Reward

Input:

```python
captured=True
```

Expected:

```
20
```

---

# Test 4: No Capture Reward

Input:

```python
captured=False
```

Expected:

```
0
```

---

# Test 5: Step Penalty

Verify:

Every call returns configured penalty.

Example:

```
-0.05
```

---

# Test 6: Total Reward Calculation

Create a known example.

Example:

```
distance_reward = 2
capture_reward = 0
step_penalty = -0.05
```

Expected:

```
1.95
```

depending on weights.

---

# Test 7: Configurable Weights

Verify:

Changing weights changes final reward.

Example:

```python
calculator1
calculator2
```

with different parameters.

Expected:

Different outputs.

---

# Documentation

Update README:

```markdown
## Current Implementation Status

Phase 7 completed:

Implemented:
- reward calculation module
- distance shaping reward
- cooperative capture reward
- step penalty

Not implemented yet:
- reinforcement learning
- training
- learning agents
```

---

# Code Quality Requirements

Before finishing:

Check:

- reward logic is isolated
- no RL code exists
- formulas are documented
- weights are configurable
- tests cover edge cases
- type hints exist

---

# Before Coding

Follow this workflow:

1. Inspect current repository.
2. Verify Phase 6 is complete.
3. Explain planned reward design.
4. Implement Phase 7 only.
5. Run tests.
6. Report results.

Do not expand scope.

---

# Definition of Done

Phase 7 is complete when:

✅ RewardCalculator exists

✅ Distance reward works

✅ Capture reward works

✅ Step penalty works

✅ Total reward works

✅ Reward is configurable

✅ Reward tests pass

✅ Reward logic is independent

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

## 4. Reward Design Explanation

Explain mathematically:

- distance reward
- capture reward
- step penalty

## 5. Phase 8 Readiness

Explain why the environment is ready for baseline agents.

Do not implement Phase 8.