import math
from typing import List, Dict, Any

def manhattan_distance(pos1: List[int], pos2: List[int]) -> int:
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def calculate_mean_hunter_target_distance(trajectory: List[Dict[str, Any]]) -> float:
    """Mean Manhattan distance from both hunters to the target."""
    if not trajectory:
        return 0.0
    total_distance = 0.0
    for step in trajectory:
        a0_dist = manhattan_distance(step["agent_0_position"], step["target_position"])
        a1_dist = manhattan_distance(step["agent_1_position"], step["target_position"])
        total_distance += (a0_dist + a1_dist) / 2.0
    return total_distance / len(trajectory)

def calculate_hunter_separation(trajectory: List[Dict[str, Any]]) -> float:
    """Mean Manhattan distance between the two hunters."""
    if not trajectory:
        return 0.0
    total_sep = 0.0
    for step in trajectory:
        total_sep += manhattan_distance(step["agent_0_position"], step["agent_1_position"])
    return total_sep / len(trajectory)

def calculate_simultaneous_adjacency(trajectory: List[Dict[str, Any]]) -> float:
    """Fraction of timesteps where both hunters are adjacent to the target."""
    if not trajectory:
        return 0.0
    count = 0
    for step in trajectory:
        a0_dist = manhattan_distance(step["agent_0_position"], step["target_position"])
        a1_dist = manhattan_distance(step["agent_1_position"], step["target_position"])
        if a0_dist == 1 and a1_dist == 1:
            count += 1
    return count / len(trajectory)

def calculate_distinct_side_positioning(trajectory: List[Dict[str, Any]]) -> float:
    """Fraction of timesteps where both hunters are adjacent to target AND in distinct cells."""
    if not trajectory:
        return 0.0
    count = 0
    for step in trajectory:
        a0_dist = manhattan_distance(step["agent_0_position"], step["target_position"])
        a1_dist = manhattan_distance(step["agent_1_position"], step["target_position"])
        if a0_dist == 1 and a1_dist == 1:
            # Check if they occupy distinct positions
            if step["agent_0_position"] != step["agent_1_position"]:
                count += 1
    return count / len(trajectory)

def calculate_all_behavioral_metrics(trajectory: List[Dict[str, Any]]) -> Dict[str, float]:
    return {
        "mean_target_distance": calculate_mean_hunter_target_distance(trajectory),
        "mean_hunter_separation": calculate_hunter_separation(trajectory),
        "simultaneous_adjacency_fraction": calculate_simultaneous_adjacency(trajectory),
        "distinct_side_fraction": calculate_distinct_side_positioning(trajectory)
    }
