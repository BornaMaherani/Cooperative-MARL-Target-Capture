from .actions import Action
from .position import Position
from .entities import Agent
from .grid_world import GridWorld

class MovementController:
    """Handles agent movement in the GridWorld."""

    @staticmethod
    def move_agent(agent: Agent, action: Action, grid: GridWorld) -> None:
        """
        Updates the agent's position based on the action and grid boundaries.
        Only valid movements are applied.
        """
        x, y = agent.position.x, agent.position.y

        if action == Action.UP:
            y += 1
        elif action == Action.DOWN:
            y -= 1
        elif action == Action.RIGHT:
            x += 1
        elif action == Action.LEFT:
            x -= 1
        elif action == Action.STAY:
            pass

        new_pos = Position(x, y)

        if grid.is_valid_position(new_pos):
            agent.set_position(new_pos)
