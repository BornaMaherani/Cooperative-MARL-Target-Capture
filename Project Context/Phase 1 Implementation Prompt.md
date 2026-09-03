# Phase 1 Implementation Prompt
# Core Entity Modeling and Domain Objects

You are now implementing **Phase 1** of the project:

**"Emergent Cooperation in Multi-Agent Reinforcement Learning for Target Capture"**

You already have:
- the complete project context
- the Phase 0 repository foundation

Your responsibility in this phase is ONLY to design and implement the core domain entities of the simulation.

Do NOT implement the environment.

Do NOT implement movement.

Do NOT implement actions.

Do NOT implement reinforcement learning.

Do NOT implement rewards.

Do NOT implement training.

This phase is only about creating clean, reusable, and academically appropriate data structures representing the world objects.

---

# Phase 1 Objective

Create the fundamental objects required for the future GridWorld environment:

- Position
- Agent
- Target

The goal is to establish a strong object model that future phases can build upon.

At the end of this phase, the project should have:

- clear entity definitions
- type-safe data structures
- validation logic
- unit tests
- documentation of design choices

---

# Design Philosophy

Follow these principles:

## 1. Keep entities simple

Entities should represent state.

They should NOT contain environment logic.

Examples:

An Agent should know:

- its ID
- its position

An Agent should NOT know:

- how the grid works
- how movement happens
- how rewards are calculated

Those responsibilities belong to future environment components.

---

## 2. Use explicit domain modeling

Avoid using anonymous dictionaries everywhere.

Prefer meaningful classes or dataclasses.

The code should be readable by someone familiar with ML research.

Example:

Good:

```python
agent.position
```

Bad:

```python
agent["pos"]
```

---

## 3. Maintain future compatibility

The design should support future additions:

Possible future properties:

Agent:
- policy reference
- observation
- reward history

Target:
- movement strategy
- behavior model

Position:
- distance calculations

However, do NOT implement future features now.

Only create what is currently required.

---

# Required Files

Create:

```text
env/

├── __init__.py
├── entities.py
└── position.py


tests/

└── test_entities.py
```

Do not modify unrelated files unless necessary.

---

# 1. Position Class

Create a Position representation.

File:

```text
env/position.py
```

The position represents coordinates inside the GridWorld.

Required attributes:

```python
x: int
y: int
```

Example:

```python
Position(x=3, y=5)
```

---

## Position Requirements

The class should support:

### Creation

Example:

```python
p = Position(2, 4)
```

---

### Equality comparison

Two positions with the same coordinates should be equal.

Example:

```python
Position(1,2) == Position(1,2)
```

should return:

```python
True
```

---

### Representation

The object should have a readable representation.

Example:

```python
Position(x=1, y=2)
```

---

### Distance calculation

Implement Manhattan distance.

Formula:

```
distance =
abs(x1-x2) + abs(y1-y2)
```

Example:

```python
p1.distance_to(p2)
```

returns:

```python
3
```

This will be useful later for reward calculation.

---

# 2. Agent Class

Create the Agent entity.

File:

```text
env/entities.py
```

The Agent represents a hunter agent.

Required attributes:

```python
id: str
position: Position
```

Example:

```python
Agent(
    id="agent_0",
    position=Position(2,3)
)
```

---

## Agent Requirements

The Agent should support:

### Initialization

Create an agent with:

- unique identifier
- initial position


---

### Position update

Provide a simple method:

Example:

```python
agent.set_position(new_position)
```

This should only update the stored position.

It should NOT check:

- grid boundaries
- collisions

Those belong to the environment.

---

### Representation

Readable output.

Example:

```
Agent(id=agent_0, position=(2,3))
```

---

# 3. Target Class

Create the Target entity.

File:

```text
env/entities.py
```

The Target represents the moving target/prey.

Required attributes:

```python
position: Position
```

Example:

```python
Target(
    position=Position(5,5)
)
```

---

## Target Requirements

The Target should support:

### Initialization

Create target with position.

---

### Position update

Example:

```python
target.set_position(new_position)
```

Again:

Do NOT implement movement logic.

Movement belongs to future target policies.

---

### Representation

Example:

```
Target(position=(5,5))
```

---

# 4. Type Safety

Use Python typing.

Example:

```python
from dataclasses import dataclass

@dataclass
class Position:
    x: int
    y: int
```

Use type hints everywhere.

The project should be easy to understand for another researcher.

---

# 5. Export Design

Update:

```text
env/__init__.py
```

Expose the main entities.

Example:

```python
from .position import Position
from .entities import Agent, Target
```

This allows clean imports:

```python
from env import Agent, Target, Position
```

---

# 6. Testing Requirements

Create:

```text
tests/test_entities.py
```

Use pytest.

Tests should verify:

---

## Position Tests

Test:

- creation
- equality
- representation
- Manhattan distance


Example:

```python
def test_position_distance():
    p1 = Position(0,0)
    p2 = Position(3,4)

    assert p1.distance_to(p2) == 7
```

---

## Agent Tests

Test:

- correct initialization
- ID storage
- position storage
- position update


---

## Target Tests

Test:

- correct initialization
- position update


---

# 7. Documentation

Update README only if needed.

Add a small section:

```markdown
## Current Implementation Status

Phase 1 completed:

Implemented:
- Position model
- Agent entity
- Target entity

Not implemented yet:
- GridWorld
- Movement
- Actions
- Reinforcement learning
```

Do not rewrite the entire README.

---

# 8. Things NOT Allowed in This Phase

Do NOT create:

❌ environment step function

❌ action enum

❌ movement logic

❌ collision handling

❌ reward calculation

❌ RL agents

❌ neural networks

❌ training scripts

❌ visualization

❌ simulation loop

These belong to later phases.

---

# Before Coding

Follow this workflow:

1. Inspect current repository after Phase 0.
2. Confirm existing structure.
3. Explain the planned changes briefly.
4. Implement only Phase 1.
5. Run tests.
6. Report results.

Do not expand scope.

---

# Definition of Done

Phase 1 is complete when:

✅ Position class exists

✅ Agent class exists

✅ Target class exists

✅ Entities are modular

✅ Type hints are used

✅ Tests pass

✅ No environment logic exists

✅ No RL code exists

✅ Code is clean and readable

---

# Final Response Format

After implementation, provide:

## 1. Summary

Explain what was implemented.

## 2. Files Created/Modified

List files.

## 3. Testing

Report pytest results.

## 4. Design Decisions

Explain important choices.

## 5. Phase 2 Readiness

Explain why the current design is ready for GridWorld implementation.

Do not implement Phase 2.