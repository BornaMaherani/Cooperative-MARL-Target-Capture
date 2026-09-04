import pytest
from env.rewards import RewardCalculator
from env.entities import Agent, Target
from env.position import Position

def test_distance_reward_positive():
    calc = RewardCalculator(distance_weight=1.0)
    reward = calc.calculate_distance_reward(previous_distance=10, current_distance=6)
    assert reward == 4.0
    assert reward > 0

def test_distance_reward_negative():
    calc = RewardCalculator(distance_weight=1.0)
    reward = calc.calculate_distance_reward(previous_distance=5, current_distance=8)
    assert reward == -3.0
    assert reward < 0

def test_capture_reward():
    calc = RewardCalculator(capture_weight=20.0)
    assert calc.calculate_capture_reward(captured=True) == 20.0

def test_no_capture_reward():
    calc = RewardCalculator(capture_weight=20.0)
    assert calc.calculate_capture_reward(captured=False) == 0.0

def test_step_penalty():
    calc = RewardCalculator(step_penalty=-0.05)
    assert calc.calculate_step_penalty() == -0.05

def test_total_reward_calculation():
    calc = RewardCalculator()
    total = calc.calculate_total_reward(distance_reward=2.0, capture_reward=0.0, step_penalty=-0.05)
    assert pytest.approx(total) == 1.95

def test_configurable_weights():
    calc1 = RewardCalculator(distance_weight=1.0, capture_weight=20.0, step_penalty=-0.05)
    calc2 = RewardCalculator(distance_weight=2.0, capture_weight=50.0, step_penalty=-0.1)
    
    # Test distance reward differences
    assert calc1.calculate_distance_reward(10, 5) == 5.0
    assert calc2.calculate_distance_reward(10, 5) == 10.0
    
    # Test capture reward differences
    assert calc1.calculate_capture_reward(True) == 20.0
    assert calc2.calculate_capture_reward(True) == 50.0

def test_calculate_api():
    calc = RewardCalculator(distance_weight=1.0, capture_weight=20.0, step_penalty=-0.05)
    
    agents = [
        Agent("agent_0", Position(5, 5)),
        Agent("agent_1", Position(5, 7))
    ]
    target = Target(Position(5, 6))
    
    previous_positions = {
        "agent_0": Position(5, 3), # distance to (5,6) was 3. Now is 1. (Delta = +2)
        "agent_1": Position(5, 9), # distance to (5,6) was 3. Now is 1. (Delta = +2)
        "target": Position(5, 6)   # target didn't move
    }
    
    # Total previous distance = 6. Total current distance = 2. Delta = 4.
    result = calc.calculate(agents, target, previous_positions, captured=True)
    
    assert result["distance_reward"] == 4.0
    assert result["capture_reward"] == 20.0
    assert result["step_penalty"] == -0.05
    assert result["total_reward"] == 4.0 + 20.0 - 0.05
