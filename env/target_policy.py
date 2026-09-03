import numpy as np
from typing import Optional
from .entities import Target
from .grid_world import GridWorld
from .actions import Action
from .movement import MovementController

class TargetPolicy:
    """Interface for target movement behavior."""
    
    def choose_action(self, target: Target, grid: GridWorld) -> Action:
        """Determines the next action for the target."""
        raise NotImplementedError


class RandomTargetPolicy(TargetPolicy):
    """
    Target selects a random valid action.
    """

    def __init__(self, seed: Optional[int] = None):
        self._rng = np.random.default_rng(seed)
        self._actions = list(Action)

    def choose_action(self, target: Target, grid: GridWorld) -> Action:
        """
        Chooses a random valid action that keeps the target within grid boundaries.
        """
        valid_actions = []
        for action in self._actions:
            # We can reuse the movement controller's logic to check position
            new_pos = MovementController.calculate_new_position(target.position, action)
            if grid.is_valid_position(new_pos):
                valid_actions.append(action)
        
        return self._rng.choice(valid_actions)
