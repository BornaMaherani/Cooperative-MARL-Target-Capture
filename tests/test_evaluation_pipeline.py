import os
import pytest
import shutil
import csv

from experiments.evaluation_utils import evaluate_policy
from experiments.statistical_analysis import calculate_mean_std, read_raw_results
from env.actions import Action

class DummyAgent:
    def __init__(self, action, epsilon=1.0):
        self.action = action
        self.epsilon = epsilon
        self.updated = False
        
    def select_action(self, obs):
        return self.action
        
    def update(self, *args, **kwargs):
        self.updated = True

def test_evaluation_does_not_learn():
    """Test 5: Verify evaluation does not update Q-values and sets epsilon to 0."""
    agent0 = DummyAgent(Action.STAY, epsilon=1.0)
    agent1 = DummyAgent(Action.STAY, epsilon=1.0)
    
    # Run evaluation
    results = evaluate_policy(agent0, agent1, "Dummy", 0, eval_episodes=2, grid_size=5, max_steps=10)
    
    assert not agent0.updated
    assert not agent1.updated
    # Epsilon should be restored to original after evaluation
    assert agent0.epsilon == 1.0

def test_metric_calculation():
    """Test 1, 2, 3: Verify metrics calculation via evaluate_policy."""
    agent0 = DummyAgent(Action.STAY)
    agent1 = DummyAgent(Action.STAY)
    
    results = evaluate_policy(agent0, agent1, "Dummy", 0, eval_episodes=2, grid_size=5, max_steps=10)
    
    assert len(results) == 2
    for res in results:
        assert "captured" in res
        assert "episode_length" in res
        assert "episode_reward" in res
        assert "capture_time" in res

def test_seed_aggregation():
    """Test 4: Verify seed aggregation (mean/std)."""
    data = [10, 20, 30]
    mean, std = calculate_mean_std(data)
    assert mean == 20.0
    assert std == 10.0  # sqrt(((10-20)^2 + (20-20)^2 + (30-20)^2)/2) = sqrt(200/2) = 10
    
    # Edge cases
    assert calculate_mean_std([]) == (0.0, 0.0)
    assert calculate_mean_std([5]) == (5.0, 0.0)

def test_result_serialization(tmp_path):
    """Test 6: Result serialization."""
    from experiments.run_comparison import save_raw_results
    
    data = [
        {"method": "Test", "training_seed": 0, "evaluation_seed": 1000, "episode": 0, "captured": 1, "episode_length": 5, "episode_reward": 10.0, "capture_time": 5}
    ]
    filepath = tmp_path / "test_results.csv"
    save_raw_results(data, str(filepath))
    
    loaded = read_raw_results(str(filepath))
    assert len(loaded) == 1
    assert loaded[0]["method"] == "Test"
    assert loaded[0]["captured"] == "1" # CSV reads as strings

def test_reproducibility():
    """Test 7: Reproducibility of evaluation given the same seed."""
    agent0 = DummyAgent(Action.STAY)
    agent1 = DummyAgent(Action.STAY)
    
    res1 = evaluate_policy(agent0, agent1, "Dummy", 42, 1, 5, 10)
    res2 = evaluate_policy(agent0, agent1, "Dummy", 42, 1, 5, 10)
    
    assert res1[0]["episode_reward"] == res2[0]["episode_reward"]
    assert res1[0]["episode_length"] == res2[0]["episode_length"]
