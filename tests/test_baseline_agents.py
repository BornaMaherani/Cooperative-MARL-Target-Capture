import pytest
from env.actions import Action
from env.position import Position
from agents.random_agent import RandomAgent
from agents.heuristic_agent import HeuristicAgent

def test_random_agent_output():
    """Test 1: Random Agent Output"""
    agent = RandomAgent()
    obs = {"agent_position": Position(0,0), "target_position": Position(5,5)}
    
    # Should always return Action enum values
    for _ in range(100):
        action = agent.select_action(obs)
        assert isinstance(action, Action)
        assert action in Action

def test_random_agent_reproducibility():
    """Test 2: Random Agent Reproducibility"""
    agent1 = RandomAgent(seed=42)
    agent2 = RandomAgent(seed=42)
    obs = {"agent_position": Position(0,0), "target_position": Position(5,5)}
    
    seq1 = [agent1.select_action(obs) for _ in range(20)]
    seq2 = [agent2.select_action(obs) for _ in range(20)]
    
    assert seq1 == seq2

def test_heuristic_agent_direction():
    """Test 3: Heuristic Agent Direction"""
    agent = HeuristicAgent()
    
    # Target is to the right
    obs1 = {"agent_position": Position(2,2), "target_position": Position(5,2)}
    assert agent.select_action(obs1) == Action.RIGHT
    
    # Target is to the left
    obs2 = {"agent_position": Position(5,2), "target_position": Position(2,2)}
    assert agent.select_action(obs2) == Action.LEFT
    
    # Target is below (y is larger)
    obs3 = {"agent_position": Position(2,2), "target_position": Position(2,5)}
    assert agent.select_action(obs3) == Action.UP
    
    # Target is above (y is smaller)
    obs4 = {"agent_position": Position(2,5), "target_position": Position(2,2)}
    assert agent.select_action(obs4) == Action.DOWN

def test_heuristic_distance_improvement():
    """Test 4: Heuristic Distance Improvement"""
    agent = HeuristicAgent()
    agent_pos = Position(2,2)
    target_pos = Position(5,5)
    obs = {"agent_position": agent_pos, "target_position": target_pos}
    
    initial_dist = agent_pos.distance_to(target_pos)
    action = agent.select_action(obs)
    
    # Calculate new position manually as GridWorld bounds aren't tested here
    new_x, new_y = agent_pos.x, agent_pos.y
    if action == Action.UP: new_y += 1
    elif action == Action.DOWN: new_y -= 1
    elif action == Action.RIGHT: new_x += 1
    elif action == Action.LEFT: new_x -= 1
        
    new_pos = Position(new_x, new_y)
    new_dist = new_pos.distance_to(target_pos)
    
    assert new_dist < initial_dist
