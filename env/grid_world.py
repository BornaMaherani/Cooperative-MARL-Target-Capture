import numpy as np
from dataclasses import dataclass
from typing import List, Optional

@dataclass(frozen=True)
class Position:
    """Represents a 2D coordinate in the GridWorld."""
    x: int
    y: int

class GridWorld:
    """
    Represents the physical space for the environment.
    Coordinates are 0-indexed: x ranges from 0 to grid_size - 1,
    y ranges from 0 to grid_size - 1.
    """

    def __init__(self, grid_size: int = 10):
        if not isinstance(grid_size, int):
            raise TypeError("grid_size must be an integer.")
        if grid_size <= 0:
            raise ValueError("grid_size must be greater than 0.")
        
        self._grid_size = grid_size
        self._rng = np.random.default_rng()

    @property
    def grid_size(self) -> int:
        """Returns the size of the grid (both width and height)."""
        return self._grid_size

    def is_valid_position(self, position: Position) -> bool:
        """Checks if a given position exists inside the grid boundaries."""
        if not isinstance(position, Position):
            raise TypeError("position must be an instance of Position.")
        return (0 <= position.x < self._grid_size) and (0 <= position.y < self._grid_size)

    def get_all_positions(self) -> List[Position]:
        """Returns a list of all valid positions in the GridWorld."""
        return [
            Position(x, y) 
            for x in range(self._grid_size) 
            for y in range(self._grid_size)
        ]

    def sample_random_position(self, seed: Optional[int] = None) -> Position:
        """
        Returns a random valid Position. 
        If a seed is provided, the sampling is deterministic.
        """
        rng = np.random.default_rng(seed) if seed is not None else self._rng
        x = int(rng.integers(0, self._grid_size))
        y = int(rng.integers(0, self._grid_size))
        return Position(x, y)
