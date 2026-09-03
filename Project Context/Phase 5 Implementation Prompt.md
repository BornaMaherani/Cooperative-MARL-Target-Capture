# Phase 5 Implementation Prompt
# Building the Core Target Capture Environment

You are now implementing **Phase 5** of the project:

**"Emergent Cooperation in Multi-Agent Reinforcement Learning for Target Capture"**

You already have:

- Phase 0: repository foundation
- Phase 1: entity modeling
- Phase 2: GridWorld core
- Phase 3: agent movement mechanics
- Phase 4: target movement policy

The repository currently contains:

- Position
- Agent
- Target
- GridWorld
- Action system
- MovementController
- TargetPolicy
- RandomTargetPolicy

Your responsibility in this phase is to combine these components into a complete simulation environment.

---

# Important Scope Restriction

This phase is ONLY about creating the core environment lifecycle.

Do NOT implement:

❌ reinforcement learning  
❌ neural networks  
❌ training loops  
❌ reward functions  
❌ capture mechanism  
❌ MARL algorithms  
❌ policy optimization  
❌ advanced observations  

Those belong to future phases.

---

# Phase 5 Objective

Create the first complete simulation environment where:

- hunters exist
- target exists
- agents can act
- target can move
- the world updates step-by-step

At the end of this phase, we should be able to run:

```python
environment.reset()

for step in range(100):
    environment.step(actions)
```

and observe the simulation progressing.

---

# Design Philosophy

## 1. Environment is the coordinator

The Environment should coordinate:

- GridWorld
- Agents
- Target
- Movement
- Time progression

It should NOT contain:

- learning logic
- reward logic
- algorithm logic

---

## 2. Keep components independent

The architecture should remain:

```
Environment
    |
    |-- GridWorld
    |
    |-- Agents
    |
    |-- Target
    |
    |-- MovementController
    |
    |-- TargetPolicy
```

The Environment uses these components.

It should not duplicate their internal logic.

---

# Required Files

Create:

```
env/

├── target_capture_env.py

tests/

└── test_environment.py

examples/

└── run_environment.py
```

Modify existing files only when necessary.

---

# Environment Class

Create:

```
env/target_capture_env.py
```

Implement:

```python
class TargetCaptureEnv:
```

---

# Constructor

The environment should accept configurable parameters.

Example:

```python
env = TargetCaptureEnv(
    grid_size=10,
    max_steps=100,
    seed=42
)
```

Required parameters:

## grid_size

Default:

```python
10
```

---

## max_steps

Maximum episode length.

Default:

```python
100
```

---

## seed

For reproducibility.

---

# Internal Components

The Environment should create and manage:

## GridWorld

Example:

```python
self.grid
```

---

## Agents

Create two hunters:

```python
agent_0

agent_1
```

Use the existing Agent class.

---

## Target

Create one target.

Use the existing Target class.

---

## Target Policy

Use:

```python
RandomTargetPolicy
```

from Phase 4.

---

# Reset Function

Implement:

```python
reset(seed=None)
```

Purpose:

Create a new episode.

It should:

1. Reset random generator.
2. Clear timestep.
3. Create new agent positions.
4. Create new target position.
5. Return initial state.

---

# Initial Position Rules

Agents and target must:

- be inside GridWorld
- not overlap initially

Example:

Invalid:

```
Agent 0:
(3,3)

Target:
(3,3)
```

The reset function must avoid this.

---

# Return Value of Reset

For now, return a simple state dictionary.

Example:

```python
{
    "agent_0": (x,y),
    "agent_1": (x,y),
    "target": (x,y)
}
```

Do NOT implement RL observations yet.

This is only for debugging.

---

# Step Function

Implement:

```python
step(actions)
```

Input:

Dictionary:

```python
{
    "agent_0": Action.RIGHT,
    "agent_1": Action.UP
}
```

---

The step function should execute the following order:

## Step 1

Apply hunter actions.

Use:

```python
MovementController
```

Do not duplicate movement logic.

---

## Step 2

Move target.

Use:

```python
RandomTargetPolicy
```

---

## Step 3

Increase timestep.

Example:

```python
self.current_step += 1
```

---

## Step 4

Create updated state.

---

## Step 5

Return environment information.

---

# Step Return Format

For now:

Return:

```python
state, info
```

Example:

```python
{
 "agent_0": position,
 "agent_1": position,
 "target": position
},
{
 "step": 10
}
```

Do NOT include reward yet.

---

# Episode Status

Implement:

```python
is_done()
```

For now:

The episode ends only when:

```python
current_step >= max_steps
```

Capture termination will be added later.

---

# Current State Function

Implement:

```python
get_state()
```

Return current world state.

Example:

```python
{
"agent_0": Position(...),
"agent_1": Position(...),
"target": Position(...)
}
```

Keep this function separate.

Future phases will replace it with observations.

---

# Rendering Support

Add:

```python
render()
```

Reuse existing information.

Simple text rendering is enough.

Example:

```
. . . . .
. H . . .
. . T . .
H . . . .
```

Where:

H = hunter

T = target

No graphical rendering yet.

---

# Testing Requirements

Create:

```
tests/test_environment.py
```

Use pytest.

---

# Test 1: Environment Creation

Verify:

- environment initializes
- grid exists
- agents exist
- target exists

---

# Test 2: Reset

Verify:

- reset returns valid state
- positions are inside grid
- no initial overlap

---

# Test 3: Step Execution

Run:

```python
env.step(actions)
```

Verify:

- timestep increases
- positions update
- returned state is valid

---

# Test 4: Reproducibility

Verify:

Two environments with same seed produce identical reset states.

Example:

```python
env1.reset(seed=42)

env2.reset(seed=42)
```

Expected:

same initial state.

---

# Test 5: Episode Limit

Run until:

```python
max_steps
```

Verify:

episode terminates.

---

# Test 6: Random Simulation

Create a small simulation:

100 random steps.

Verify:

- no crashes
- no invalid positions
- no entity leaves the grid

---

# Example Script

Create:

```
examples/run_environment.py
```

The script should:

1. Create environment.
2. Reset.
3. Run 50 random actions.
4. Render each step.
5. Print timestep information.

Example:

```
Step: 0

. . . .
. H . .
. . T .
H . . .

Step: 1
...
```

---

# Documentation

Update README:

Add:

```markdown
## Current Implementation Status

Phase 5 completed:

Implemented:
- complete simulation environment
- reset function
- step function
- agent-target interaction loop
- environment state management

Not implemented yet:
- capture condition
- rewards
- reinforcement learning
- training
```

---

# Code Quality Requirements

Before finishing:

Check:

- Environment does not duplicate movement logic.
- Components remain independent.
- Type hints exist.
- Functions have docstrings.
- No RL code exists.
- No reward logic exists.

---

# Before Coding

Follow this workflow:

1. Inspect current repository.
2. Verify Phase 1-4 components exist.
3. Explain planned modifications.
4. Implement Phase 5 only.
5. Run tests.
6. Report results.

Do not expand scope.

---

# Definition of Done

Phase 5 is complete when:

✅ TargetCaptureEnv exists

✅ reset() works

✅ step() works

✅ Agents and target interact in simulation

✅ State can be retrieved

✅ Rendering works

✅ Random simulation runs

✅ Tests pass

✅ Reproducibility works

✅ No reward exists

✅ No RL exists

---

# Final Response Format

After implementation, provide:

## 1. Summary

Explain what was implemented.

## 2. Files Created/Modified

List files.

## 3. Testing Results

Show pytest output.

## 4. Architecture Explanation

Explain how:

- Environment
- GridWorld
- Agents
- Target
- Movement

work together.

## 5. Phase 6 Readiness

Explain why the environment is ready for adding capture mechanics.

Do not implement Phase 6.