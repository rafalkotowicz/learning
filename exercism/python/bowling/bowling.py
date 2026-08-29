"""Bowling exercise implementation."""


class BowlingGame:
    """Track rolls in a bowling game and compute the final score."""

    _MAX_PINS_PER_ROLL = 10
    _TOTAL_FRAMES = 10

    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        """Record a roll after validating current game state and roll value."""
        self._validate_single_roll_value(pins)

        candidate_rolls = self._rolls + [pins]
        self._validate_roll_sequence(candidate_rolls, require_complete=False)
        self._rolls = candidate_rolls

    def score(self):
        """Return score for a complete game."""
        self._validate_roll_sequence(self._rolls, require_complete=True)

        total_score = 0
        roll_position = 0

        frame_counter = 0
        while frame_counter < self._TOTAL_FRAMES:
            if (first_roll := self._rolls[roll_position]) == self._MAX_PINS_PER_ROLL:
                total_score += (
                    self._MAX_PINS_PER_ROLL
                    + self._rolls[roll_position + 1]
                    + self._rolls[roll_position + 2]
                )
                roll_position += 1
                frame_counter += 1
                continue

            second_roll = self._rolls[roll_position + 1]
            if (frame_sum := first_roll + second_roll) == self._MAX_PINS_PER_ROLL:
                total_score += self._MAX_PINS_PER_ROLL + self._rolls[roll_position + 2]
            else:
                total_score += frame_sum

            roll_position += 2
            frame_counter += 1

        return total_score

    @classmethod
    def _validate_single_roll_value(cls, pins):
        if pins < 0:
            raise ValueError("Negative roll is invalid")
        if pins > cls._MAX_PINS_PER_ROLL:
            raise ValueError("Pin count exceeds pins on the lane")

    @classmethod
    def _validate_roll_sequence(cls, rolls, require_complete):
        """Validate game structure; optionally require game to be complete."""
        roll_position = 0

        frame_counter = 1
        while frame_counter < cls._TOTAL_FRAMES:
            roll_position = cls._validate_regular_frame(rolls, roll_position, require_complete)
            if roll_position is None:
                return
            frame_counter += 1

        completion_result = cls._validate_tenth_frame(rolls, roll_position, require_complete)
        if completion_result is None:
            return

        if completion_result != len(rolls):
            raise ValueError("Cannot roll after game is over")

    @classmethod
    def _validate_regular_frame(cls, rolls, roll_position, require_complete):
        if roll_position >= len(rolls):
            if require_complete:
                raise ValueError("Score cannot be taken until the end of the game")
            return None

        if (first_roll := rolls[roll_position]) == cls._MAX_PINS_PER_ROLL:
            return roll_position + 1

        if (second_position := roll_position + 1) >= len(rolls):
            if require_complete:
                raise ValueError("Score cannot be taken until the end of the game")
            return None

        second_roll = rolls[second_position]
        if first_roll + second_roll > cls._MAX_PINS_PER_ROLL:
            raise ValueError("Pin count exceeds pins on the lane")

        return roll_position + 2

    @classmethod
    def _validate_tenth_frame(cls, rolls, roll_position, require_complete):
        if (first_roll := cls._read_roll_or_none(rolls, roll_position, require_complete)) is None:
            return None

        second_position = roll_position + 1
        second_roll = cls._read_roll_or_none(rolls, second_position, require_complete)
        if second_roll is None:
            return None

        frame_sum = first_roll + second_roll

        if first_roll != cls._MAX_PINS_PER_ROLL and frame_sum > cls._MAX_PINS_PER_ROLL:
            raise ValueError("Pin count exceeds pins on the lane")

        if cls._MAX_PINS_PER_ROLL not in (first_roll, frame_sum):
            return roll_position + 2

        third_position = roll_position + 2
        if (third_roll := cls._read_roll_or_none(rolls, third_position, require_complete)) is None:
            return None

        if first_roll == cls._MAX_PINS_PER_ROLL and second_roll != cls._MAX_PINS_PER_ROLL:
            if second_roll + third_roll > cls._MAX_PINS_PER_ROLL:
                raise ValueError("Invalid fill balls")

        return roll_position + 3

    @classmethod
    def _read_roll_or_none(cls, rolls, roll_position, require_complete):
        """Return roll value, None for incomplete game, or raise when completion is required."""
        if roll_position >= len(rolls):
            if require_complete:
                raise ValueError("Score cannot be taken until the end of the game")
            return None
        return rolls[roll_position]
