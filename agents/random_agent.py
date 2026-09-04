import numpy as np
from typing import Dict, Any, Optional
from env.actions import Action
from .base_agent import BaseAgent

class RandomAgent(BaseAgent):
    """
    An agent that selects actions entirely randomly, ignoring all observations.
    """

    def __init__(self, seed: Optional[int] = None):
        """
        Args:
            seed: Optional seed for reproducible randomness.
        """
        self._rng = np.random.default_rng(seed)
        self._actions = list(Action)

    def select_action(self, observation: Dict[str, Any]) -> Action:
        """
        Returns a random valid Action.
        """
        return self._rng.choice(self._actions)
