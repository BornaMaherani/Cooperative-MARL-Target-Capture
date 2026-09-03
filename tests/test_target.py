import pytest
from env import Target, Position, GridWorld, Action, MovementController
from env.target_policy import RandomTargetPolicy

def test_target_creation():
    target = Target(Position(5, 5))
    assert target.position == Position(5, 5)

def test_random_policy_output():
    grid = GridWorld(10)
    target = Target(Position(5, 5))
    policy = RandomTargetPolicy(seed=42)
    
    for _ in range(50):
        action = policy.choose_action(target, grid)
        assert action in Action
        assert isinstance(action, Action)

def test_reproducibility():
    grid = GridWorld(10)
    target1 = Target(Position(5, 5))
    target2 = Target(Position(5, 5))
    
    policy1 = RandomTargetPolicy(seed=42)
    policy2 = RandomTargetPolicy(seed=42)
    
    actions1 = [policy1.choose_action(target1, grid) for _ in range(10)]
    actions2 = [policy2.choose_action(target2, grid) for _ in range(10)]
    
    assert actions1 == actions2

def test_target_movement():
    grid = GridWorld(10)
    target = Target(Position(5, 5))
    
    MovementController.move_target(target, Action.UP, grid)
    assert target.position == Position(5, 6)
    
    MovementController.move_target(target, Action.LEFT, grid)
    assert target.position == Position(4, 6)

def test_boundary_handling():
    grid = GridWorld(10)
    target = Target(Position(0, 0))
    
    # Move left against boundary
    MovementController.move_target(target, Action.LEFT, grid)
    assert target.position == Position(0, 0)
    
    # Move down against boundary
    MovementController.move_target(target, Action.DOWN, grid)
    assert target.position == Position(0, 0)

def test_multiple_steps():
    grid = GridWorld(10)
    target = Target(Position(5, 5))
    policy = RandomTargetPolicy(seed=99)
    
    for _ in range(100):
        action = policy.choose_action(target, grid)
        MovementController.move_target(target, action, grid)
        
        # Verify target never leaves the GridWorld
        assert grid.is_valid_position(target.position)
