# Phase 3 Implementation Prompt
# Agent Movement Mechanics

You are now implementing **Phase 3** of the project:

**"Emergent Cooperation in Multi-Agent Reinforcement Learning for Target Capture"**

You already have:

- Phase 0: repository foundation
- Phase 1: core entities
- Phase 2: GridWorld implementation

The repository currently contains:

- Position
- Agent
- Target
- GridWorld

Your task in this phase is ONLY to implement agent movement mechanics.

---

# Important Scope Restriction

This phase is ONLY about moving agents inside the GridWorld.

Do NOT implement:

❌ target movement  
❌ capture logic  
❌ reward calculation  
❌ episode management  
❌ environment step function  
❌ reinforcement learning  
❌ training loops  
❌ observations for agents  

Those belong to future phases.

---

# Phase 3 Objective

Create a clean movement system that allows hunter agents to perform discrete actions and update their positions inside the GridWorld.

At the end of this phase:

A user should be able to:

1. Create a GridWorld.
2. Create an Agent.
3. Apply an action.
4. Move the Agent.
5. Verify that movement respects grid boundaries.

---

# Design Philosophy

Follow these principles:

## 1. Keep movement independent

Movement logic should not belong inside the Agent class.

The Agent stores state.

A separate component should handle movement.

Reason:

Later, RL algorithms will decide actions, but the environment will execute them.

---

## 2. Clear separation

Responsibilities:

### Agent

Knows:

- id
- current position

Does NOT know:

- grid boundaries
- valid moves
- actions


### GridWorld

Knows:

- world dimensions
- valid positions


### Movement System

Knows:

- action interpretation
- position transitions

---

# Required Files

Create:

```text
env/

├── actions.py
├── movement.py

tests/

└── test_movement.py
```

Modify existing files only if required.

---

# 1. Action Definition

Create:

```text
env/actions.py
```

Implement a clear action representation.

Use Python Enum.

Example:

```python
from enum import Enum


class Action(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    STAY = 4
```

---

# Action Requirements

The action system should:

- be readable
- avoid magic numbers
- be easy to extend later

Example:

Good:

```python
Action.UP
```

Bad:

```python
0
```

---

# 2. Movement Component

Create:

```text
env/movement.py
```

Implement a movement utility.

Example:

```python
class MovementController:
```

The exact name can differ if you have a better design.

---

# Movement Responsibility

The movement component should:

Input:

- Agent
- Action
- GridWorld

Output:

- Updated agent position

Example:

```python
move_agent(
    agent,
    Action.UP,
    grid
)
```

---

# Movement Rules

Implement:

## UP

Increase y coordinate.

Example:

Before:

```text
(2,2)
```

After:

```text
(2,3)
```

---

## DOWN

Decrease y coordinate.

---

## RIGHT

Increase x coordinate.

---

## LEFT

Decrease x coordinate.

---

## STAY

No movement.

---

# Coordinate Convention

Use the same convention from previous phases:

Position:

```python
Position(x,y)
```

where:

x = horizontal axis

y = vertical axis


Document this clearly.

---

# Boundary Handling

Movement must respect GridWorld boundaries.

Example:

Grid:

```text
10 x 10
```

Valid:

```text
0 <= x < 10
0 <= y < 10
```

---

Example:

Agent:

```python
Position(0,5)
```

Action:

```python
Action.LEFT
```

Expected:

Agent stays:

```python
Position(0,5)
```

Do not allow invalid positions.

---

# Collision Handling

Do NOT implement collision between agents.

Do NOT implement obstacles.

For this phase:

Agents can theoretically occupy the same cell.

Collision rules belong to future phases.

---

# Agent Update Rules

The movement system should:

1. Calculate the intended new position.
2. Check if it is valid using GridWorld.
3. Update the Agent only if valid.

Do not duplicate boundary logic.

Use:

```python
grid.is_valid_position()
```

---

# Example Usage

The final API should allow something similar:

```python
from env import Agent, Position, GridWorld
from env.actions import Action
from env.movement import MovementController


grid = GridWorld(10)

agent = Agent(
    id="agent_0",
    position=Position(5,5)
)

MovementController.move_agent(
    agent,
    Action.UP,
    grid
)

print(agent.position)
```

Expected:

```text
Position(5,6)
```

---

# Testing Requirements

Create:

```text
tests/test_movement.py
```

Use pytest.

---

# Test 1: Basic Movement

Test:

UP

Example:

```python
agent = Agent(
    "agent_0",
    Position(5,5)
)

move(agent, Action.UP)

assert agent.position == Position(5,6)
```

---

# Test 2: All Directions

Test:

- UP
- DOWN
- LEFT
- RIGHT
- STAY

Verify correct coordinate changes.

---

# Test 3: Boundary Protection

Test:

Agent at:

```python
Position(0,0)
```

Actions:

LEFT

DOWN


Expected:

Position remains:

```python
Position(0,0)
```

---

# Test 4: Grid Independence

Verify that movement logic uses GridWorld validation.

Do not duplicate boundary conditions.

---

# Test 5: Multiple Agents

Create two agents.

Move them independently.

Verify that each keeps its own position.

No collision logic is expected.

---

# Documentation

Update README status section.

Add:

```markdown
## Current Implementation Status

Phase 3 completed:

Implemented:
- discrete action definition
- agent movement mechanics
- boundary-aware movement

Not implemented yet:
- target movement
- capture mechanism
- rewards
- reinforcement learning
```

---

# Code Quality Requirements

Before finishing:

Check:

- type hints
- docstrings
- readable naming
- no duplicated logic
- no unnecessary dependencies

The implementation should be easy for another researcher to understand.

---

# Before Coding

Follow this workflow:

1. Inspect current repository.
2. Confirm Phase 1 and Phase 2 components exist.
3. Explain planned changes.
4. Implement Phase 3 only.
5. Run tests.
6. Report results.

Do not expand scope.

---

# Definition of Done

Phase 3 is complete when:

✅ Action enum exists

✅ Movement component exists

✅ Agents can move

✅ Boundary rules work

✅ Movement tests pass

✅ Agent state updates correctly

✅ No target movement exists

✅ No capture logic exists

✅ No RL code exists

---

# Final Response Format

After implementation, provide:

## 1. Summary

What was implemented.

## 2. Files Created/Modified

List all files.

## 3. Testing Results

Show pytest output.

## 4. Design Decisions

Explain:

- action representation
- movement architecture
- boundary handling

## 5. Phase 4 Readiness

Explain why the project is ready for target movement implementation.

Do not implement Phase 4.