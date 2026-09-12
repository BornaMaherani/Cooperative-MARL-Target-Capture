import pytest
import json
from analysis.trajectory_analysis import TrajectoryRecorder
from analysis.behavioral_metrics import (
    manhattan_distance, 
    calculate_mean_hunter_target_distance,
    calculate_hunter_separation,
    calculate_simultaneous_adjacency,
    calculate_distinct_side_positioning
)

def test_trajectory_recorder(tmp_path):
    """Test 1 & Test 7: Trajectory recording and serialization."""
    recorder = TrajectoryRecorder()
    recorder.set_metadata("Test", 0, 1000, 5, 10)
    
    # Dummy step
    recorder.record_step(
        step=0,
        state={"agent_0": type('Pos', (), {'x': 0, 'y': 0})(), "agent_1": type('Pos', (), {'x': 1, 'y': 0})(), "target": type('Pos', (), {'x': 1, 'y': 1})()},
        actions={"agent_0": "UP", "agent_1": "DOWN"},
        info={"target_action": "STAY", "captured": False},
        reward=1.0
    )
    
    assert len(recorder.trajectory) == 1
    assert recorder.trajectory[0]["step"] == 0
    assert recorder.trajectory[0]["agent_0_position"] == [0, 0]
    
    filepath = tmp_path / "test_traj.json"
    recorder.save(str(filepath))
    
    loaded = TrajectoryRecorder.load(str(filepath))
    assert loaded.metadata["method"] == "Test"
    assert len(loaded.trajectory) == 1
    assert loaded.trajectory[0]["agent_1_position"] == [1, 0]

def test_distance_metrics():
    """Test 3 & Test 4: Distance calculations."""
    trajectory = [
        {
            "agent_0_position": [0, 0],
            "agent_1_position": [2, 0],
            "target_position": [1, 1]
        }
    ]
    
    # Target distance: A0 is (0,0)->(1,1) = 2. A1 is (2,0)->(1,1) = 2. Mean = 2.0
    assert calculate_mean_hunter_target_distance(trajectory) == 2.0
    
    # Hunter separation: (0,0)->(2,0) = 2
    assert calculate_hunter_separation(trajectory) == 2.0

def test_adjacency_metrics():
    """Test 5 & Test 6: Adjacency and Distinct-Side Positioning."""
    # Step 1: Adjacency but same cell
    # Step 2: Adjacency distinct cells
    # Step 3: Not adjacent
    trajectory = [
        {
            "agent_0_position": [0, 1],
            "agent_1_position": [0, 1],
            "target_position": [0, 0]
        },
        {
            "agent_0_position": [1, 0],
            "agent_1_position": [0, 1],
            "target_position": [0, 0]
        },
        {
            "agent_0_position": [5, 5],
            "agent_1_position": [5, 5],
            "target_position": [0, 0]
        }
    ]
    
    # Sim. Adjacency: Step 1 (yes), Step 2 (yes), Step 3 (no) -> 2/3
    assert calculate_simultaneous_adjacency(trajectory) == pytest.approx(2/3)
    
    # Distinct side: Step 1 (no, same cell), Step 2 (yes), Step 3 (no) -> 1/3
    assert calculate_distinct_side_positioning(trajectory) == pytest.approx(1/3)
