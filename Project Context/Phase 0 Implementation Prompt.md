# Phase 0 Implementation Prompt
# Project Initialization & Repository Foundation

You are now implementing **Phase 0** of the project:

**"Emergent Cooperation in Multi-Agent Reinforcement Learning for Target Capture"**

You already have the complete project context.

Your responsibility in this phase is ONLY to initialize a clean, academic-quality software repository foundation.

Do NOT implement any environment logic.

Do NOT implement agents.

Do NOT implement reinforcement learning.

Do NOT create simulations.

Do NOT create unnecessary abstractions.

The goal is to prepare a professional project structure that will support future development phases.

---

# Phase 0 Objective

Create the initial repository structure and development foundation.

At the end of this phase, the project should have:

- a clean folder organization
- dependency management
- basic documentation
- testing infrastructure
- configuration for future development

The repository should look like a serious academic ML project on GitHub.

---

# Development Principles

Follow these principles:

## 1. Keep it minimal

Only create what is required for future phases.

Do not add:

- Docker
- CI/CD pipelines
- deployment files
- unnecessary frameworks
- unused dependencies

---

## 2. Research-oriented structure

The repository should clearly separate:

- environment code
- algorithms
- experiments
- tests
- documentation
- results

The structure should support future ML experimentation.

---

# Required Repository Structure

Create the following structure:

```
Cooperative-MARL-Target-Capture/

│
├── env/
│   └── __init__.py
│
├── agents/
│   └── __init__.py
│
├── algorithms/
│   └── __init__.py
│
├── experiments/
│   └── __init__.py
│
├── tests/
│   └── __init__.py
│
├── results/
│   ├── plots/
│   └── gifs/
│
├── configs/
│
├── docs/
│
├── README.md
│
├── requirements.txt
│
├── .gitignore
│
└── main.py
```

If the current repository already exists, inspect it first and adapt carefully.

Do not delete existing useful files without explanation.

---

# Folder Responsibilities

Document the purpose of each folder.

Expected meaning:

## env/

Contains all future environment-related components:

Examples:

- GridWorld
- entities
- state transitions
- rendering

Currently empty except initialization.

---

## agents/

Contains future agent implementations.

Examples:

- random agent
- heuristic agent
- learning agents

Currently empty.

---

## algorithms/

Contains future reinforcement learning algorithms.

Examples:

- Q-learning
- actor-critic
- cooperative MARL algorithms

Currently empty.

---

## experiments/

Contains future:

- training scripts
- evaluation scripts
- experiment runners

Currently empty.

---

## tests/

Contains automated tests.

Prepare this folder for pytest.

No actual environment tests are needed yet.

---

## results/

Stores generated experimental outputs.

Structure:

```
results/

├── plots/

└── gifs/
```

---

## configs/

Stores future configuration files.

Examples:

- environment parameters
- training parameters

Do not create configuration files yet.

---

## docs/

Stores future technical documentation.

---

# README.md Requirements

Create a professional initial README.

It should contain:

---

## Title

```
# Emergent Cooperation in Multi-Agent Reinforcement Learning for Target Capture
```

---

## Project Overview

Explain briefly:

- this project studies cooperative behavior in multi-agent reinforcement learning
- multiple agents learn to capture a moving target
- the goal is to investigate emergence of cooperation

Do not claim implemented features that do not exist yet.

---

## Current Status

Clearly state:

```
Current phase:
Phase 0 - Project Initialization

Implemented:
- Repository structure
- Development foundation

Not implemented yet:
- Environment
- Agents
- Reinforcement learning algorithms
- Experiments
```

---

## Future Roadmap

Add a simple roadmap:

```
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
```

---

## Installation

Add placeholder instructions:

Example:

```bash
git clone <repository-url>

cd Cooperative-MARL-Target-Capture

pip install -r requirements.txt
```

Do not add fake commands.

---

# requirements.txt

Create a minimal requirements file.

Only include packages that are actually needed at this stage.

For Phase 0:

Recommended:

```
pytest
numpy
matplotlib
```

Do NOT add:

- torch
- ray
- rllib
- pettingzoo

Those belong to later phases.

---

# .gitignore

Create a standard Python .gitignore.

Include:

```
__pycache__/
*.pyc
.venv/
venv/
.env
.idea/
.vscode/
results/*
```

Do not ignore important source files.

---

# main.py

Create a minimal entry point.

It should NOT implement project logic.

Example:

```python
def main():
    print("Cooperative MARL Target Capture Project")
    print("Current stage: Phase 0 - Initialization")


if __name__ == "__main__":
    main()
```

The purpose is only to verify that the repository runs.

---

# Testing Setup

Configure pytest compatibility.

A simple test should verify that the project imports correctly.

Create:

```
tests/test_setup.py
```

The test should confirm that the repository foundation is valid.

Do not test environment behavior because it does not exist yet.

---

# Code Quality Requirements

Before finishing:

Check:

- no unnecessary files
- no unused dependencies
- no broken imports
- clean naming
- clear documentation

The repository should be understandable by another researcher.

---

# Before Making Changes

Follow this workflow:

1. Inspect current repository state.
2. Explain briefly what you plan to create.
3. Implement Phase 0 only.
4. Run available tests.
5. Report results.

Do not silently expand the scope.

---

# Definition of Done

Phase 0 is complete only when:

✅ Repository structure exists

✅ README is created

✅ requirements.txt exists

✅ .gitignore exists

✅ main.py runs successfully

✅ pytest can run

✅ No ML/environment code has been added

✅ Structure is ready for Phase 1

---

# Final Response Format

After implementation, provide:

## 1. Summary

What was created.

## 2. Files Added

List all created files.

## 3. Verification

Show:

- main.py execution result
- pytest result

## 4. Design Decisions

Explain any structural decisions.

## 5. Ready for Phase 1

Confirm that the repository is ready for environment implementation.

Do not implement Phase 1.