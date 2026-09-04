from typing import Dict, Any
from env.actions import Action
from .base_agent import BaseAgent

class HeuristicAgent(BaseAgent):
    """
    An agent that uses a simple greedy heuristic to minimize Manhattan distance
    to the target. It does not cooperate with other agents.
    """

    def select_action(self, observation: Dict[str, Any]) -> Action:
        """
        Moves toward the target by reducing horizontal or vertical distance.
        """
        agent_pos = observation["agent_position"]
        target_pos = observation["target_position"]
        
        dx = target_pos.x - agent_pos.x
        dy = target_pos.y - agent_pos.y
        
        # Priority: close horizontal distance first, then vertical
        if dx > 0:
            return Action.RIGHT
        elif dx < 0:
            return Action.LEFT
        elif dy > 0:
            return Action.UP
        elif dy < 0:
            return Action.DOWN
            
        # Already on top of target (shouldn't happen before capture, but just in case)
        return Action.STAY
