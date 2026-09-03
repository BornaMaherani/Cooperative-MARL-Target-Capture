# Phase 4 Implementation Prompt
# Target Entity Behavior and Movement Policy

You are now implementing **Phase 4** of the project:

**"Emergent Cooperation in Multi-Agent Reinforcement Learning for Target Capture"**

You already have:

- Phase 0: repository foundation
- Phase 1: entity modeling
- Phase 2: GridWorld implementation
- Phase 3: agent movement mechanics

The current repository contains:

- Position
- Agent
- Target
- GridWorld
- Action system
- Agent movement controller

Your responsibility in this phase is ONLY to implement target behavior and target movement.

---

# Important Scope Restriction

This phase is ONLY about target dynamics.

Do NOT implement:

❌ environment class  
❌ environment step function  
❌ agent-target interaction  
❌ capture logic  
❌ reward calculation  
❌ episode management  
❌ reinforcement learning  
❌ training loops  
❌ observations  

Those belong to later phases.

---

# Phase 4 Objective

Create a modular target movement system.

The target should:

- exist in the GridWorld
- have a movement policy
- choose actions
- update its position
- respect world boundaries

The design should allow replacing the target behavior later.

For example:

Future possibilities:

- random target
- escaping target
- learned target policy

---

# Design Philosophy

## 1. Separate Target from Target Policy

The Target object stores state.

The Target Policy decides behavior.

Do NOT put movement intelligence inside Target.

---

Responsibilities:

## Target

Knows:

- current position


Does NOT know:

- how to move
- how to choose actions
- grid rules


---

## Target Policy

Knows:

- how to select an action

Example:

Random movement.

---

## GridWorld

Knows:

- valid positions

---

## MovementController

Already exists.

Reuse it.

Do NOT duplicate movement logic.

---

# Required Files

Create:

```text id="a4u2dx"
env/

├── target_policy.py

tests/

└── test_target.py
```

Modify existing files only when necessary.

---

# 1. Target Policy Interface

Create:

```text
env/target_policy.py
```

Implement a simple policy abstraction.

Example:

```python
class TargetPolicy:
    def choose_action(self, target, grid):
        pass
```

The exact implementation can differ.

The important requirement:

The target behavior must be separated from the Target entity.

---

# 2. Random Target Policy

Implement:

```python
class RandomTargetPolicy:
```

Purpose:

The target selects random valid movements.

Possible actions:

```text
UP
DOWN
LEFT
RIGHT
STAY
```

Reuse the existing Action enum.

Do NOT create a second action system.

---

# Random Policy Requirements

The policy should:

- select only valid actions
- respect grid boundaries
- support reproducibility using seed

Example:

```python
policy = RandomTargetPolicy(seed=42)
```

The same seed should produce the same sequence of actions.

---

# 3. Target Movement Functionality

The Target class already exists.

Extend it only if necessary.

Do not make Target responsible for policy decisions.

A possible usage:

```python
target_action = policy.choose_action(
    target,
    grid
)

MovementController.move_target(
    target,
    target_action,
    grid
)
```

If a separate movement abstraction is cleaner, implement it.

Do not duplicate agent movement logic unnecessarily.

---

# 4. Movement Reuse

The project already has agent movement mechanics.

Avoid writing:

```python
new_x = target.x + dx
new_y = target.y + dy
```

again.

Reuse existing movement utilities.

The code should have a single source of truth for movement rules.

---

# 5. Target Movement Rules

The target follows the same GridWorld rules:

Valid:

```text
0 <= x < grid_size
0 <= y < grid_size
```

Invalid moves:

- leaving the grid

should result in:

- staying in place

or another clearly documented behavior.

Choose one behavior and document it.

---

# 6. Randomness Handling

Do not use uncontrolled randomness.

Avoid:

```python
import random
random.choice(...)
```

without control.

Use a dedicated random generator.

Example:

```python
numpy.random.Generator
```

The behavior should be reproducible.

---

# Example Usage

The final API should allow:

```python
from env import Target, Position, GridWorld
from env.target_policy import RandomTargetPolicy


grid = GridWorld(10)

target = Target(
    position=Position(5,5)
)

policy = RandomTargetPolicy(seed=42)

action = policy.choose_action(
    target,
    grid
)

print(action)
```

The target should receive an action decision.

---

# Testing Requirements

Create:

```text
tests/test_target.py
```

Use pytest.

---

# Test 1: Target Creation

Verify:

- target initializes correctly
- position is stored correctly

Example:

```python
target = Target(Position(5,5))

assert target.position == Position(5,5)
```

---

# Test 2: Random Policy Output

Verify:

The policy always returns:

```text
UP
DOWN
LEFT
RIGHT
STAY
```

and nothing else.

---

# Test 3: Reproducibility

Verify:

```python
policy1 = RandomTargetPolicy(seed=42)
policy2 = RandomTargetPolicy(seed=42)
```

produce the same action sequence.

---

# Test 4: Target Movement

Verify:

Target position changes correctly after a valid action.

Example:

UP:

```text
(5,5)
→
(5,6)
```

---

# Test 5: Boundary Handling

Example:

Target:

```text
Position(0,0)
```

Action:

```text
LEFT
```

Expected:

Target remains inside grid.

---

# Test 6: Multiple Steps

Run:

100 random target movements.

Verify:

The target never leaves the GridWorld.

---

# Documentation

Update README status section:

```markdown
## Current Implementation Status

Phase 4 completed:

Implemented:
- target movement
- random target policy
- reproducible target behavior

Not implemented yet:
- full environment
- agent-target interaction
- capture mechanism
- rewards
- reinforcement learning
```

---

# Code Quality Requirements

Before finishing:

Check:

- no duplicated movement logic
- type hints everywhere
- clear class responsibilities
- meaningful names
- minimal dependencies

The code should be understandable by an AI/ML researcher.

---

# Before Coding

Follow this workflow:

1. Inspect current repository.
2. Confirm Phase 3 components exist.
3. Explain planned changes.
4. Implement Phase 4 only.
5. Run tests.
6. Report results.

Do not expand scope.

---

# Definition of Done

Phase 4 is complete when:

✅ Target entity works

✅ Target policy exists

✅ Random target movement works

✅ Movement rules are respected

✅ Randomness is reproducible

✅ Tests pass

✅ Movement logic is not duplicated

✅ No environment class exists

✅ No capture logic exists

✅ No RL code exists

---

# Final Response Format

After implementation, provide:

## 1. Summary

What was implemented.

## 2. Files Created/Modified

List files.

## 3. Testing Results

Show pytest output.

## 4. Design Decisions

Explain:

- target-policy separation
- randomness handling
- movement reuse

## 5. Phase 5 Readiness

Explain why the project is ready to combine agents and target into a complete environment.

Do not implement Phase 5.