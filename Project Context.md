# Project Context Prompt
## Cooperative Multi-Agent Reinforcement Learning for Target Capture

You are assisting us in building a research-oriented Artificial Intelligence project that will be published as an open-source GitHub repository and used as an academic portfolio project for graduate applications.

Your first task is NOT implementation.

Before writing any code, you must deeply understand the motivation, scientific purpose, architecture, scope, constraints, and expected quality level of this project.

A separate implementation roadmap will be provided later.

For now:
- Do not start coding.
- Do not create files.
- Do not over-engineer the project.
- Do not introduce unnecessary infrastructure.
- Focus on understanding the project.

After understanding this context, summarize:
1. Your understanding of the research problem.
2. The expected software architecture.
3. The main machine learning concepts involved.
4. The major implementation risks.
5. Any assumptions that should be clarified before development.

---

# 1. Project Goal

The project is called:

# Emergent Cooperation in Multi-Agent Reinforcement Learning for Target Capture

The main research question is:

"Can multiple autonomous agents learn cooperative behavior through reinforcement learning in order to capture a moving target?"

The purpose of this project is NOT to build a production system.

The purpose is to demonstrate:

- understanding of Multi-Agent Reinforcement Learning (MARL)
- ability to design a custom RL environment
- understanding of cooperation between agents
- understanding of reward shaping
- ability to design experiments
- ability to analyze learning behavior
- ability to create a clean academic GitHub repository

The final repository should look like a small research project rather than a simple programming assignment.

The project should be understandable by:
- AI researchers
- machine learning professors
- graduate admission committees

The priority is:

1. Scientific clarity
2. Correct implementation
3. Reproducible experiments
4. Clean code
5. Good documentation

---

# 2. Project Scope

This is a one-week project developed by two people.

Therefore, the project must remain focused and realistic.

The project should NOT include:

- Docker
- Ray
- RLlib
- cloud infrastructure
- distributed training
- complicated deployment systems
- excessive engineering

The project should focus on:

- environment design
- reinforcement learning algorithms
- experimental comparison
- visualization
- scientific explanation

The final result should be small but high-quality.

---

# 3. Core Idea

We create a simple GridWorld environment.

The environment contains:

- two hunter agents
- one moving target

The hunters must learn to cooperate and capture the target.

The target moves through the environment using a simple predefined strategy.

The important scientific aspect is:

The agents should learn coordination instead of independently chasing the target.

The project studies whether cooperation can emerge through learning.

---

# 4. Environment Design

The environment is a 2D discrete GridWorld.

Example:

Grid size:

10 × 10

Entities:

## Hunter Agents

Two intelligent agents:

Agent 1

Agent 2


They are controlled by reinforcement learning algorithms.

---

## Target

One moving target.

The target is not learned.

It follows a predefined movement strategy.

Possible strategies:

- random movement
- simple escape heuristic

The target exists to create a cooperative challenge.

---

# 5. Environment Rules

The environment must define:

- grid boundaries
- agent movement
- target movement
- collisions
- episode termination
- capture condition

The implementation must avoid ambiguous behavior.

Important functions should conceptually exist:

```
reset()

step()

render()

is_target_captured()
```

The environment should be deterministic when using a fixed random seed.

---

# 6. Action Space

Each agent has five possible actions:

```
UP
DOWN
LEFT
RIGHT
STAY
```

Actions are discrete.

Invalid actions should be handled consistently.

Examples:

- moving outside the grid
- moving into forbidden locations

The behavior should be documented.

---

# 7. Observation Space

To keep the project achievable, the observation can initially be simplified.

Each agent receives:

- its own position
- target position
- teammate position

Example observation:

```
[
agent_x,
agent_y,
target_x,
target_y,
other_agent_x,
other_agent_y
]
```

The main goal is to study cooperation, not partial observability complexity.

However, the design should keep future extension possible.

---

# 8. Capture Condition

The target is captured when the hunters successfully surround it.

A clear mathematical rule must be implemented.

Example:

If both hunters occupy valid neighboring positions around the target:

```
capture = True
```

The exact rule should be explicitly defined.

The capture condition must be deterministic.

---

# 9. Reward Function

Reward design is one of the most important parts of this project.

The reward should encourage:

- approaching the target
- cooperation
- fast capture

A possible formulation:

```
Total Reward =
Distance Reward
+
Team Capture Reward
+
Step Penalty
```

---

## Distance Reward

Agents receive positive reward when they reduce their distance to the target.

Example:

```
previous_distance - current_distance
```

Moving closer:

positive reward

Moving farther:

negative reward

---

## Team Capture Reward

When the target is successfully captured:

Example:

```
+20
```

Both agents should receive the cooperative reward.

This encourages teamwork.

---

## Step Penalty

Each step receives a small negative reward.

Example:

```
-0.05
```

This encourages efficient behavior.

---

# 10. Algorithms

The project should contain several approaches for comparison.

The goal is not only to train a model.

The goal is to analyze differences between learning strategies.

---

# Experiment 1

## Random Agents

Purpose:

- validate environment
- establish a weak baseline

Expected result:

Very low capture performance.

---

# Experiment 2

## Independent Q-Learning

Each agent learns separately.

Purpose:

Show limitations of independent learning.

Important concept:

Multi-agent non-stationarity.

Each agent sees other learning agents as part of the environment.

---

# Experiment 3

## Cooperative Multi-Agent Reinforcement Learning

Implement a cooperative learning approach.

A lightweight approach is preferred.

Possible options:

- Multi-Agent Actor-Critic
- simplified MAPPO-style approach
- shared policy learning

The implementation should prioritize correctness and understanding over complexity.

---

# 11. Scientific Questions

The final project should answer questions like:

1. Can agents learn cooperative target capture?

2. Does cooperative learning outperform independent learning?

3. How important is reward shaping?

4. Does shared team reward improve coordination?

5. Do learned agents behave differently from greedy agents?

6. Are agents actually cooperating or simply following individual strategies?

---

# 12. Evaluation Metrics

The project should not only report reward.

Important metrics:

## Capture Rate

Percentage of successful episodes.

Example:

```
successful episodes / total episodes
```

---

## Average Capture Time

How many steps are needed to capture the target.

---

## Average Episode Reward

Total accumulated reward.

---

## Learning Curve

Plot performance during training.

---

# 13. Visualization

The final repository should include visual demonstrations.

Examples:

Before training:

```
random agents chasing target
```

After training:

```
agents coordinate and capture target
```

Generate:

- GIF demonstrations
- reward curves
- comparison plots

Visualization is important because it communicates learned behavior.

---

# 14. Recommended Repository Structure

The project should have a clean structure.

Example:

```
Cooperative-MARL-Target-Capture/

│
├── env/
│   └── target_capture_env.py
│
├── agents/
│   ├── random_agent.py
│   └── heuristic_agent.py
│
├── algorithms/
│   ├── q_learning.py
│   └── cooperative_marl.py
│
├── experiments/
│   ├── train.py
│   └── evaluate.py
│
├── results/
│   ├── plots/
│   └── gifs/
│
├── tests/
│
├── README.md
│
└── requirements.txt
```

This structure may evolve if a better design is found.

---

# 15. Technology Stack

Preferred:

Python

Libraries:

- numpy
- pytorch
- matplotlib
- gymnasium
- pettingzoo (optional)
- tqdm
- imageio

The project should avoid unnecessary dependencies.

---

# 16. Two Person Development

This project is developed by two people.

The responsibilities should be separated but integrated.

---

## Developer A

Environment and evaluation focus.

Responsibilities:

- GridWorld implementation
- environment logic
- movement rules
- capture condition
- rendering
- visualization
- experiment evaluation
- plotting

---

## Developer B

Machine learning focus.

Responsibilities:

- reinforcement learning algorithms
- training loop
- reward implementation
- baseline algorithms
- cooperative learning method
- hyperparameter experiments

---

## Shared Responsibilities

Both developers:

- understand the complete architecture
- review each other's code
- analyze results
- write README
- prepare final presentation

---

# 17. Development Philosophy

Do not create a huge complicated system.

A smaller scientifically correct project is better than a large unstable project.

Follow these principles:

- modular code
- readable implementation
- meaningful comments
- reproducible experiments
- clean Git history
- good documentation

Avoid:

- unnecessary abstraction
- premature optimization
- complicated frameworks

---

# 18. Expected Final GitHub Quality

The repository should contain:

- clear README
- project motivation
- architecture explanation
- mathematical formulation
- algorithm explanation
- experiment setup
- results
- discussion
- limitations
- future improvements

The README should feel similar to a small research paper.

---

# 19. Future Improvement Possibilities

The project may later be extended with:

- partial observability
- obstacles
- larger number of agents
- different reward functions
- MAPPO
- centralized critics
- more advanced MARL algorithms

However, these are NOT required for the first version.

The first version must be complete and polished.

---

# Current Task

You are currently in the project understanding phase.

Do not implement anything yet.

Confirm that you understand:

- the research motivation
- the technical scope
- the software architecture
- the machine learning objectives
- the expected GitHub quality

Then wait for the next instruction, where the implementation roadmap and development phases will be provided.