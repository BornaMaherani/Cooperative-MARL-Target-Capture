from dataclasses import dataclass
from .position import Position

@dataclass
class Agent:
    id: str
    position: Position

    def set_position(self, new_position: Position) -> None:
        """Update the agent's position."""
        self.position = new_position


@dataclass
class Target:
    position: Position

    def set_position(self, new_position: Position) -> None:
        """Update the target's position."""
        self.position = new_position
