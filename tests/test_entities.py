import pytest
from env import Position, Agent, Target

def test_position_creation():
    p = Position(2, 4)
    assert p.x == 2
    assert p.y == 4

def test_position_equality():
    assert Position(1, 2) == Position(1, 2)
    assert Position(1, 2) != Position(2, 1)

def test_position_representation():
    p = Position(x=1, y=2)
    assert repr(p) == "Position(x=1, y=2)"

def test_position_distance():
    p1 = Position(0, 0)
    p2 = Position(3, 4)
    assert p1.distance_to(p2) == 7

def test_agent_initialization():
    agent = Agent(id="agent_0", position=Position(2, 3))
    assert agent.id == "agent_0"
    assert agent.position == Position(2, 3)

def test_agent_set_position():
    agent = Agent(id="agent_0", position=Position(2, 3))
    new_pos = Position(5, 5)
    agent.set_position(new_pos)
    assert agent.position == new_pos

def test_agent_representation():
    agent = Agent(id="agent_0", position=Position(2, 3))
    # Dataclasses default repr includes the attributes. 
    # Because position is also a dataclass, its repr is included.
    assert repr(agent) == "Agent(id='agent_0', position=Position(x=2, y=3))"

def test_target_initialization():
    target = Target(position=Position(5, 5))
    assert target.position == Position(5, 5)

def test_target_set_position():
    target = Target(position=Position(5, 5))
    new_pos = Position(1, 1)
    target.set_position(new_pos)
    assert target.position == new_pos

def test_target_representation():
    target = Target(position=Position(5, 5))
    assert repr(target) == "Target(position=Position(x=5, y=5))"
