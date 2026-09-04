from typing import List
from .entities import Agent, Target

class CaptureChecker:
    """Checks if the target is captured by the agents."""
    
    @staticmethod
    def is_captured(agents: List[Agent], target: Target) -> bool:
        """
        The target is captured when BOTH hunter agents are adjacent to the target.
        Adjacency is defined as a Manhattan distance of exactly 1.
        """
        if not agents or len(agents) < 2:
            return False
            
        for agent in agents:
            if agent.position.distance_to(target.position) != 1:
                return False
                
        return True
