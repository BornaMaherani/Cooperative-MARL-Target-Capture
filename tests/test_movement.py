import pytest
from env import Agent, Position, GridWorld, Action, MovementController

def test_basic_movement():
    grid = GridWorld(10)
    agent = Agent(id="agent_0", position=Position(5, 5))
    
    MovementController.move_agent(agent, Action.UP, grid)
    assert agent.position == Position(5, 6)

def test_all_directions():
    grid = GridWorld(10)
    agent = Agent(id="agent_0", position=Position(5, 5))
    
    MovementController.move_agent(agent, Action.UP, grid)
    assert agent.position == Position(5, 6)
    
    MovementController.move_agent(agent, Action.DOWN, grid)
    assert agent.position == Position(5, 5)
    
    MovementController.move_agent(agent, Action.LEFT, grid)
    assert agent.position == Position(4, 5)
    
    MovementController.move_agent(agent, Action.RIGHT, grid)
    assert agent.position == Position(5, 5)
    
    MovementController.move_agent(agent, Action.STAY, grid)
    assert agent.position == Position(5, 5)

def test_boundary_protection():
    grid = GridWorld(10)
    agent = Agent(id="agent_0", position=Position(0, 0))
    
    MovementController.move_agent(agent, Action.LEFT, grid)
    assert agent.position == Position(0, 0)
    
    MovementController.move_agent(agent, Action.DOWN, grid)
    assert agent.position == Position(0, 0)

def test_grid_independence():
    grid = GridWorld(5)
    agent = Agent(id="agent_0", position=Position(4, 4))
    
    MovementController.move_agent(agent, Action.UP, grid)
    assert agent.position == Position(4, 4)
    
    MovementController.move_agent(agent, Action.RIGHT, grid)
    assert agent.position == Position(4, 4)

def test_multiple_agents():
    grid = GridWorld(10)
    agent1 = Agent(id="agent_1", position=Position(2, 2))
    agent2 = Agent(id="agent_2", position=Position(5, 5))
    
    MovementController.move_agent(agent1, Action.UP, grid)
    MovementController.move_agent(agent2, Action.LEFT, grid)
    
    assert agent1.position == Position(2, 3)
    assert agent2.position == Position(4, 5)
    
    # Verify they can theoretically occupy the same cell
    agent3 = Agent(id="agent_3", position=Position(4, 4))
    agent4 = Agent(id="agent_4", position=Position(4, 5))
    MovementController.move_agent(agent3, Action.UP, grid)
    assert agent3.position == Position(4, 5)
    assert agent4.position == Position(4, 5)
