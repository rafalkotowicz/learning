"""Two-bucket puzzle solver."""

from collections import deque

BUCKET_ONE = "one"
BUCKET_TWO = "two"


def measure(
    bucket_one: int, bucket_two: int, goal: int, start_bucket: str
) -> tuple[int, str, int]:
    """Return the minimum move count and final bucket state for the goal."""
    if start_bucket not in {BUCKET_ONE, BUCKET_TWO}:
        raise ValueError("start_bucket must be 'one' or 'two'.")

    if goal > max(bucket_one, bucket_two):
        raise ValueError("Goal cannot be larger than both buckets.")

    if start_bucket == BUCKET_ONE:
        initial_state = (bucket_one, 0)
        forbidden_state = (0, bucket_two)
    else:
        initial_state = (0, bucket_two)
        forbidden_state = (bucket_one, 0)

    state_queue: deque[tuple[int, tuple[int, int]]] = deque([(1, initial_state)])
    visited_states: set[tuple[int, int]] = {initial_state}

    while state_queue:
        move_count, current_state = state_queue.popleft()
        volume_one, volume_two = current_state

        if volume_one == goal:
            return move_count, BUCKET_ONE, volume_two
        if volume_two == goal:
            return move_count, BUCKET_TWO, volume_one

        next_states = _generate_next_states(volume_one, volume_two, bucket_one, bucket_two)
        for next_state in next_states:
            if next_state == forbidden_state or next_state in visited_states:
                continue
            visited_states.add(next_state)
            state_queue.append((move_count + 1, next_state))

    raise ValueError("Cannot measure the requested goal with these buckets.")


def _generate_next_states(
    volume_one: int, volume_two: int, bucket_one: int, bucket_two: int
) -> set[tuple[int, int]]:
    """Generate all states reachable from the current state in one move."""
    transfer_one_to_two = min(volume_one, bucket_two - volume_two)
    transfer_two_to_one = min(volume_two, bucket_one - volume_one)

    return {
        (bucket_one, volume_two),
        (volume_one, bucket_two),
        (0, volume_two),
        (volume_one, 0),
        (volume_one - transfer_one_to_two, volume_two + transfer_one_to_two),
        (volume_one + transfer_two_to_one, volume_two - transfer_two_to_one),
    }
