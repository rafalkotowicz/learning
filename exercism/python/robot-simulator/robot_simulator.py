"""Robot Simulator exercise implementation."""

from typing import NamedTuple

EAST = "east"
NORTH = "north"
WEST = "west"
SOUTH = "south"

_DIRECTIONS = (NORTH, EAST, SOUTH, WEST)
_TURN_RIGHT = "R"
_TURN_LEFT = "L"
_ADVANCE = "A"


class Step(NamedTuple):
    """2D movement step for a direction."""

    delta_x: int
    delta_y: int


_STEP_BY_DIRECTION = {
    NORTH: Step(0, 1),
    EAST: Step(1, 0),
    SOUTH: Step(0, -1),
    WEST: Step(-1, 0),
}


class Robot:
    """Represent robot position and orientation on a 2D grid."""

    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        """Create a robot with initial direction and coordinates."""
        if direction not in _DIRECTIONS:
            raise ValueError("Invalid direction.")

        self._direction = direction
        self._x_pos = x_pos
        self._y_pos = y_pos

    @property
    def direction(self):
        """Return current robot direction."""
        return self._direction

    @property
    def coordinates(self):
        """Return current robot coordinates as a tuple."""
        return (self._x_pos, self._y_pos)

    def move(self, instructions):
        """Apply movement instructions and update robot state."""
        for instruction in instructions:
            if instruction == _TURN_RIGHT:
                self._turn_right()
            elif instruction == _TURN_LEFT:
                self._turn_left()
            elif instruction == _ADVANCE:
                self._advance()
            else:
                raise ValueError("Invalid instruction.")

    def _turn_right(self):
        direction_index = _DIRECTIONS.index(self._direction)
        self._direction = _DIRECTIONS[(direction_index + 1) % len(_DIRECTIONS)]

    def _turn_left(self):
        direction_index = _DIRECTIONS.index(self._direction)
        self._direction = _DIRECTIONS[(direction_index - 1) % len(_DIRECTIONS)]

    def _advance(self):
        step = _STEP_BY_DIRECTION[self._direction]
        self._x_pos += step.delta_x
        self._y_pos += step.delta_y
