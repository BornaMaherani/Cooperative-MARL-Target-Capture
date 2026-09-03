# Phase 9 Implementation Prompt
# Independent Q-Learning Baseline

You are now implementing **Phase 9** of the project:

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
- Phase 8: baseline agents and evaluation

The current repository contains:

- TargetCaptureEnv
- CaptureChecker
- RewardCalculator
- RandomAgent
- HeuristicAgent
- Baseline evaluation framework

Your responsibility in this phase is ONLY to implement an Independent Q-Learning baseline.

---

# Important Scope Restriction

This phase is ONLY about a simple tabular reinforcement learning agent.

Do NOT implement:

❌ Deep Q Networks (DQN)

❌ PyTorch models

❌ Neural networks

❌ Policy gradients

❌ Actor-Critic

❌ MAPPO

❌ Advanced MARL algorithms

❌ Distributed training

The purpose is to create a simple learning baseline.

---

# Phase 9 Objective

Implement Independent Q-Learning where each hunter agent learns its own policy independently.

The goal is to compare:

```
Random Agent
        ↓
Heuristic Agent
        ↓
Independent Q-Learning Agent
```

The scientific purpose is to investigate:

- whether agents can learn useful behavior
- limitations of independent learning
- difficulty of cooperation without explicit coordination

---

# Scientific Background

In Independent Q-Learning:

Each agent treats other agents as part of the environment.

Each agent maintains its own Q-function:

For agent i:

\[
Q_i(s,a)
\]

Agents do not share Q-tables.

They do not directly coordinate.

This creates a simple example of multi-agent non-stationarity.

---

# Design Philosophy

## 1. Keep RL algorithm separate from environment

The environment should not know:

- Q-values
- exploration strategy
- learning updates

The learner should interact with the environment through:

- observation/state
- action
- reward
- next state

---

## 2. Keep implementation simple

This is a research baseline.

Prioritize:

- correctness
- readability
- reproducibility

Not performance.

---

# Required Files

Create:

```text
algorithms/

├── __init__.py
├── q_learning.py


agents/

└── q_learning_agent.py


experiments/

├── train_q_learning.py
└── evaluate_q_learning.py


tests/

└── test_q_learning.py
```

---

# 1. Q-Learning Agent

Create:

```
agents/q_learning_agent.py
```

Implement:

```python
class QLearningAgent:
```

The agent should contain:

- Q-table
- learning parameters
- action selection logic
- update rule

---

# Agent Parameters

Support:

```python
learning_rate
gamma
epsilon
epsilon_decay
min_epsilon
```

Example:

```python
agent = QLearningAgent(
    learning_rate=0.1,
    gamma=0.95,
    epsilon=1.0
)
```

Do not hard-code values.

---

# 2. State Representation

Use a simple discrete state representation.

Do NOT implement neural embeddings.

A state can be represented as:

```python
(
agent_x,
agent_y,
target_x,
target_y
)
```

For multiple agents:

Each agent only receives:

- its own position
- target position

Do NOT include teammate information.

This intentionally represents independent learning.

---

# 3. Action Selection

Implement epsilon-greedy exploration.

During training:

With probability epsilon:

choose random action.

Otherwise:

choose action with highest Q-value.

Example:

\[
a =
\begin{cases}
random action & probability \epsilon\\
argmax Q(s,a) & otherwise
\end{cases}
\]

---

# 4. Q Update Rule

Implement standard Q-learning:

\[
Q(s,a)
=
Q(s,a)
+
\alpha
[
r+\gamma max Q(s',a')-Q(s,a)
]
\]

Where:

alpha:

learning rate

gamma:

discount factor

---

# 5. Multi-Agent Setup

Create two independent learners:

Example:

```python
agent_0 = QLearningAgent()

agent_1 = QLearningAgent()
```

They must have:

- separate Q-tables
- separate learning updates

Do NOT share parameters.

---

# 6. Training Script

Create:

```
experiments/train_q_learning.py
```

The script should:

1. Create environment.
2. Create two Q-learning agents.
3. Run episodes.
4. Select actions.
5. Execute environment steps.
6. Calculate rewards.
7. Update Q-tables.
8. Record metrics.

---

# Training Loop Structure

Conceptually:

```
for episode:

    state = env.reset()

    while not done:

        action_0 = agent_0.select_action(state_0)

        action_1 = agent_1.select_action(state_1)

        next_state = env.step(actions)

        reward = calculate_reward()

        agent_0.update()

        agent_1.update()
```

Keep implementation modular.

---

# 7. Exploration Scheduling

Implement epsilon decay.

Example:

After each episode:

```
epsilon =
max(
min_epsilon,
epsilon * decay
)
```

The exact values should be configurable.

---

# 8. Evaluation Script

Create:

```
experiments/evaluate_q_learning.py
```

Purpose:

Evaluate trained agents without exploration.

During evaluation:

epsilon = 0

Metrics:

- Capture Rate
- Average Episode Length
- Average Reward

---

# 9. Saving and Loading

Implement simple persistence.

The Q-table should be saveable.

Example:

```
results/checkpoints/
```

Use a simple format:

- pickle
- json

Do not introduce complex frameworks.

---

# Testing Requirements

Create:

```
tests/test_q_learning.py
```

---

# Test 1: Agent Initialization

Verify:

- Q-table exists
- parameters are stored

---

# Test 2: Action Selection

Verify:

Agent always returns valid actions.

---

# Test 3: Q Update

Create a simple known example.

Verify:

Q-value changes after update.

---

# Test 4: Exploration

With epsilon=1:

Actions should be random.

---

# Test 5: Exploitation

With epsilon=0:

Agent chooses highest Q-value action.

---

# Test 6: Training Smoke Test

Run:

few episodes.

Verify:

- no crashes
- Q-table changes
- rewards are collected

---

# Metrics

Track:

## Training Reward

Average reward per episode.

---

## Capture Rate

Successful captures / total episodes.

---

## Episode Length

Average number of steps.

---

# Visualization

Create simple plots if easy:

```
results/plots/

q_learning_reward.png
q_learning_capture_rate.png
```

Do not over-engineer visualization.

---

# Documentation

Update README:

```markdown
## Current Implementation Status

Phase 9 completed:

Implemented:
- independent Q-learning baseline
- tabular learning agent
- training loop
- evaluation pipeline

Not implemented yet:
- deep reinforcement learning
- cooperative MARL algorithms
- MAPPO
```

---

# Code Quality Requirements

Before finishing:

Check:

- environment and learning are separated
- Q-learning logic is modular
- training is reproducible
- no deep learning dependencies
- tests exist
- results can be regenerated

---

# Before Coding

Follow this workflow:

1. Inspect current repository.
2. Verify Phase 8 completion.
3. Explain planned RL architecture.
4. Implement Phase 9 only.
5. Run tests.
6. Report results.

Do not expand scope.

---

# Definition of Done

Phase 9 is complete when:

✅ QLearningAgent exists

✅ Q-table learning works

✅ epsilon-greedy works

✅ Q-update works

✅ two independent agents can train

✅ evaluation works

✅ metrics are collected

✅ tests pass

✅ no neural networks exist

✅ no advanced MARL exists

---

# Final Response Format

After implementation, provide:

## 1. Summary

What was implemented.

## 2. Files Created/Modified

List files.

## 3. Testing Results

Show pytest output.

## 4. Learning Algorithm Explanation

Explain:

- state representation
- epsilon-greedy
- Q-update rule

## 5. Baseline Comparison

Compare:

- Random
- Heuristic
- Independent Q-learning

## 6. Phase 10 Readiness

Explain why the project is ready for cooperative learning.

Do not implement Phase 10.