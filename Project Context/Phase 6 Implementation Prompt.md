# Phase 6 Implementation Prompt
# Target Capture Mechanism and Terminal Conditions

You are now implementing **Phase 6** of the project:

**"Emergent Cooperation in Multi-Agent Reinforcement Learning for Target Capture"**

You already have:

- Phase 0: repository foundation
- Phase 1: entity modeling
- Phase 2: GridWorld core
- Phase 3: agent movement mechanics
- Phase 4: target movement policy
- Phase 5: complete simulation environment

The current repository contains:

- Position
- Agent
- Target
- GridWorld
- Action system
- MovementController
- TargetPolicy
- RandomTargetPolicy
- TargetCaptureEnv

Your responsibility in this phase is ONLY to implement the capture mechanism and episode termination based on successful target capture.

---

# Important Scope Restriction

This phase is ONLY about defining when the target is captured.

Do NOT implement:

❌ reward functions  
❌ reinforcement learning  
❌ training loops  
❌ neural networks  
❌ observations  
❌ MARL algorithms  
❌ learning policies  

Those belong to later phases.

---

# Phase 6 Objective

Transform the environment from a movement simulation into a target capture simulation.

The environment should now be able to answer:

"Did the hunters successfully cooperate and capture the target?"

At the end of this phase:

The environment should support:

1. Checking whether capture happened.
2. Ending an episode after successful capture.
3. Reporting success information.
4. Testing capture scenarios deterministically.

---

# Capture Design Requirements

The capture condition must be:

- deterministic
- simple
- explainable
- easy to modify later

The first version of the capture rule:

The target is captured when BOTH hunter agents are adjacent to the target.

---

# Capture Definition

Use Manhattan distance:

```
distance =
abs(agent_x - target_x)
+
abs(agent_y - target_y)
```

A hunter is considered close to the target when:

```
distance == 1
```

Capture occurs when:

```
agent_0_close AND agent_1_close
```

Example:

Valid capture:

```
H . H
. T .
```

Invalid:

```
H . .
. T .
. . H
```

because diagonal distance is not enough.

---

# Design Philosophy

## 1. Keep capture logic independent

Do not put capture logic inside:

- Agent
- Target
- GridWorld
- MovementController

Capture is a property of the environment.

---

## 2. Create a dedicated component

Implement capture checking separately.

Recommended:

```text
env/

├── capture.py
```

Containing:

```python
class CaptureChecker:
```

or an equivalent clean design.

---

# Required Files

Create:

```text
env/

├── capture.py

tests/

└── test_capture.py
```

Modify:

```text
env/target_capture_env.py
```

only where necessary.

---

# 1. Capture Checker

Create:

```text
env/capture.py
```

Implement a capture checking utility.

Example:

```python
is_captured(
    agents,
    target
) -> bool
```

The exact API can differ.

Requirements:

Input:

- hunter agents
- target

Output:

Boolean:

```
True
```

or

```
False
```

---

# 2. Capture Logic Requirements

The function should:

1. Calculate distance from each hunter to target.
2. Check adjacency condition.
3. Return capture status.

Do not:

- modify entities
- move objects
- end episodes

The checker only answers a question.

---

# 3. Integrate With Environment

Update:

```text
env/target_capture_env.py
```

The environment should now use capture checking.

After every step:

The order should become:

1. Apply hunter actions.
2. Move target.
3. Update timestep.
4. Check capture.
5. Update episode status.
6. Return state and info.

---

# 4. Episode Termination

The environment currently terminates only because of max steps.

Now add:

Successful termination:

```
terminated = True
```

when:

```
target captured
```

---

Timeout remains:

```
truncated = True
```

when:

```
max_steps reached
```

Keep these two concepts separate.

---

# 5. Step Return Format

Update the environment step output.

Use:

```python
state, info
```

with termination information.

Example:

```python
{
    "step": 20,
    "captured": True
}
```

The exact structure can differ.

The important thing:

Capture information must be observable.

---

# 6. Environment State

Add:

```python
self.captured
```

or equivalent.

The environment should remember whether capture happened.

Reset must clear it.

Example:

After reset:

```
captured = False
```

After success:

```
captured = True
```

---

# Testing Requirements

Create:

```text
tests/test_capture.py
```

Use pytest.

---

# Test 1: Successful Capture

Create:

Target:

```
Position(5,5)
```

Agents:

```
Agent 0 -> Position(5,4)

Agent 1 -> Position(5,6)
```

Expected:

```
captured == True
```

---

# Test 2: Not Captured

Create:

Target:

```
Position(5,5)
```

Agents:

```
Agent 0 -> Position(1,1)

Agent 1 -> Position(8,8)
```

Expected:

```
captured == False
```

---

# Test 3: Diagonal Case

Example:

Target:

```
Position(5,5)
```

Agent:

```
Position(6,6)
```

Expected:

Not considered captured.

---

# Test 4: Environment Termination

Create a scenario where capture happens.

Run:

```python
env.step(actions)
```

Verify:

```
terminated == True
```

---

# Test 5: Reset After Capture

After successful capture:

Call:

```python
env.reset()
```

Verify:

```
captured == False
```

---

# Documentation

Update README status:

```markdown
## Current Implementation Status

Phase 6 completed:

Implemented:
- target capture condition
- capture checking module
- successful episode termination

Not implemented yet:
- rewards
- reinforcement learning
- training
- MARL algorithms
```

---

# Code Quality Requirements

Before finishing:

Check:

- capture logic is isolated
- no duplicated distance calculations
- no reward logic exists
- no RL code exists
- functions have clear names
- tests cover edge cases

---

# Before Coding

Follow this workflow:

1. Inspect current repository.
2. Confirm Phase 5 environment exists.
3. Explain planned changes.
4. Implement Phase 6 only.
5. Run tests.
6. Report results.

Do not expand scope.

---

# Definition of Done

Phase 6 is complete when:

✅ CaptureChecker exists

✅ Capture condition is deterministic

✅ Environment detects capture

✅ Successful capture terminates episodes

✅ Timeout and success are separated

✅ Capture tests pass

✅ Reset clears capture state

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

## 4. Capture Rule Explanation

Explain mathematically how capture works.

## 5. Phase 7 Readiness

Explain why the environment is ready for reward design.

Do not implement Phase 7.