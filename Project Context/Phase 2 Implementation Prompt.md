# Phase 2 Implementation Prompt
# GridWorld Core Implementation

You are now implementing **Phase 2** of the project:

**"Emergent Cooperation in Multi-Agent Reinforcement Learning for Target Capture"**

You already have:

- Phase 0: repository foundation
- Phase 1: core entity modeling

The current repository contains:

- Position
- Agent
- Target

Your responsibility in this phase is ONLY to implement the core GridWorld representation.

---

# Important Scope Restriction

This phase is ONLY about creating the world/grid abstraction.

Do NOT implement:

❌ agent movement  
❌ target movement  
❌ action space  
❌ environment step function  
❌ reward calculation  
❌ reinforcement learning  
❌ training loops  
❌ simulation episodes  
❌ rendering  

Those belong to future phases.

---

# Phase 2 Objective

Create a clean GridWorld component that represents the physical space where future agents and targets will exist.

The GridWorld should be responsible for:

- storing grid dimensions
- validating positions
- checking boundaries
- providing basic world-level utilities

The GridWorld should NOT control entities.

---

# Design Philosophy

Follow these principles:

## 1. Separation of concerns

The GridWorld knows:

- the size of the world
- valid coordinates

The GridWorld does NOT know:

- how agents behave
- how targets move
- how rewards work

---

## 2. Research-quality design

The code should be:

- modular
- readable
- testable
- easy to extend

Future phases will build on this component.

---

# Required Files

Create:

```text
env/

├── __init__.py
├── grid_world.py

tests/

└── test_grid_world.py
```

Do not modify unrelated files.

---

# GridWorld Class

Create:

```text
env/grid_world.py
```

Implement:

```python
class GridWorld:
```

---

# Constructor

The GridWorld should accept:

```python
grid_size: int
```

Example:

```python
grid = GridWorld(grid_size=10)
```

Default value:

```python
grid_size = 10
```

---

# Grid Representation

The world is a square grid:

Example:

```
10 x 10
```

Valid coordinates:

```
x: 0 → 9
y: 0 → 9
```

The coordinate convention must be clearly documented.

Use the same coordinate system defined in Phase 1:

```python
Position(x, y)
```

---

# Required Properties

The GridWorld should expose:

Example:

```python
grid.size
```

or:

```python
grid.grid_size
```

The naming should be consistent and readable.

---

# Position Validation

Implement:

```python
is_valid_position(position: Position) -> bool
```

Purpose:

Check whether a position exists inside the grid.

Example:

```python
grid = GridWorld(10)

grid.is_valid_position(Position(5,5))
```

returns:

```python
True
```

---

Example:

```python
grid.is_valid_position(Position(-1,5))
```

returns:

```python
False
```

---

# Boundary Checking

Implement internal logic:

A position is valid only if:

```
0 <= x < grid_size

AND

0 <= y < grid_size
```

Do not duplicate this logic in multiple places.

Create a single source of truth.

---

# Coordinate Utilities

Implement a small number of useful helper functions.

Do not over-engineer.

Required:

## Get all valid positions

Implement:

```python
get_all_positions()
```

Example output:

```python
[
 Position(0,0),
 Position(0,1),
 ...
]
```

This will be useful later for:

- random initialization
- testing
- sampling

---

# Position Sampling

Implement:

```python
sample_random_position(seed=None)
```

Purpose:

Return a random valid Position.

Requirements:

- deterministic with seed
- uses controlled randomness
- never returns invalid positions

Example:

```python
grid.sample_random_position(seed=42)
```

should always return the same position.

---

# Randomness Requirements

Do NOT use uncontrolled:

```python
random
```

calls everywhere.

Use a dedicated random generator.

Example approach:

```python
numpy.random.Generator
```

or equivalent.

The implementation should be reproducible.

---

# Error Handling

The GridWorld should handle invalid inputs.

Examples:

## Invalid grid size

```python
GridWorld(grid_size=0)
```

should raise a clear error.

Acceptable:

```python
ValueError
```

with meaningful message.

---

## Invalid position type

If a function expects:

```python
Position
```

and receives something else, fail clearly.

Avoid silent failures.

---

# Testing Requirements

Create:

```text
tests/test_grid_world.py
```

Use pytest.

---

## Test 1: Creation

Verify:

- GridWorld initializes
- size is stored correctly

Example:

```python
grid = GridWorld(10)

assert grid.grid_size == 10
```

---

## Test 2: Valid Positions

Test:

```python
Position(0,0)

Position(5,5)

Position(9,9)
```

Expected:

True

---

## Test 3: Invalid Positions

Test:

```python
Position(-1,0)

Position(10,10)

Position(0,-2)
```

Expected:

False

---

## Test 4: Position Generation

Verify:

```python
get_all_positions()
```

returns:

```
grid_size * grid_size
```

positions.

Example:

For:

```
10x10
```

Expected:

```
100 positions
```

---

## Test 5: Random Sampling

Verify:

- returned position is valid
- same seed produces same result

Example:

```python
p1 = grid.sample_random_position(seed=42)

p2 = grid.sample_random_position(seed=42)

assert p1 == p2
```

---

# Documentation

Update README only with a small status update.

Add:

```markdown
## Current Implementation Status

Phase 2 completed:

Implemented:
- GridWorld core
- position validation
- random position sampling

Not implemented yet:
- movement
- actions
- environment dynamics
- reinforcement learning
```

Do not rewrite the complete README.

---

# Code Quality Requirements

Before finishing:

Check:

- clear naming
- type hints
- docstrings
- no duplicated logic
- no unnecessary dependencies

The implementation should be understandable by someone reading an academic repository.

---

# Before Coding

Follow this workflow:

1. Inspect the current repository.
2. Confirm Phase 1 components exist.
3. Explain planned modifications.
4. Implement only Phase 2.
5. Run tests.
6. Report results.

Do not expand the scope.

---

# Definition of Done

Phase 2 is complete when:

✅ GridWorld class exists

✅ Grid size is configurable

✅ Position validation works

✅ Invalid sizes are handled

✅ Random position sampling works

✅ Reproducibility works

✅ Tests pass

✅ No movement logic exists

✅ No environment logic exists

✅ No RL code exists

---

# Final Response Format

After implementation, provide:

## 1. Summary

What was implemented.

## 2. Files Created/Modified

List files.

## 3. Testing Results

Show pytest result.

## 4. Design Decisions

Explain:

- coordinate convention
- randomness handling
- GridWorld responsibilities

## 5. Phase 3 Readiness

Explain why the GridWorld is ready for adding movement mechanics.

Do not implement Phase 3.