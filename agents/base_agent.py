from typing import Dict, Any
from env.actions import Action
from env.position import Position

class BaseAgent:
    """
    Abstract interface for all agents interacting with the environment.
    Agents take an observation and return an action.
    """

    def select_action(self, observation: Dict[str, Any]) -> Action:
        """
        Determines the next action based on the given observation.
        
        Args:
            observation: A dictionary containing the environment state, e.g.:
                {
                    "agent_position": Position(...),
                    "target_position": Position(...)
                }
                
        Returns:
            The selected Action enum.
        """
        raise NotImplementedError("Subclasses must implement select_action")
