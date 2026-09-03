from dataclasses import dataclass

@dataclass
class Position:
    x: int
    y: int

    def distance_to(self, other: 'Position') -> int:
        """Calculate the Manhattan distance to another Position."""
        return abs(self.x - other.x) + abs(self.y - other.y)
