"""Camicia game simulation."""

from collections import deque
from dataclasses import dataclass, field

PAYMENT_VALUES = {"J": 1, "Q": 2, "K": 3, "A": 4}
NUMBER_PLACEHOLDER = "N"


@dataclass
class _GameState:
    """Mutable state of an ongoing game."""

    player_decks: list[deque[str]]
    next_player_index: int = 0
    central_pile: list[str] = field(default_factory=list)
    tricks_count: int = 0
    played_cards_count: int = 0
    penalty_remaining: int = 0
    payment_owner_index: int | None = None


def _normalize_deck(player_deck: deque[str]) -> tuple[str, ...]:
    """Normalize a deck for loop detection.

    Number cards share one placeholder because only payment cards affect rules.
    """
    return tuple(
        card if card in PAYMENT_VALUES else NUMBER_PLACEHOLDER for card in player_deck
    )


def _loop_signature(game_state: _GameState) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """Create a loop-detection signature from both normalized decks."""
    return (
        _normalize_deck(game_state.player_decks[0]),
        _normalize_deck(game_state.player_decks[1]),
    )


def _collect_pile(collector_deck: deque[str], central_pile: list[str]) -> None:
    """Move the full central pile to the bottom of the collector's deck."""
    collector_deck.extend(central_pile)
    central_pile.clear()


def _game_result(status_name: str, game_state: _GameState) -> dict[str, str | int]:
    """Build result payload in the expected Exercism format."""
    return {
        "status": status_name,
        "cards": game_state.played_cards_count,
        "tricks": game_state.tricks_count,
    }


def _start_of_round(game_state: _GameState) -> bool:
    """Return whether the game is at the start of a round."""
    return not game_state.penalty_remaining and not game_state.central_pile


def _handle_unable_to_play(
    game_state: _GameState, opponent_player_index: int
) -> dict[str, str | int] | None:
    """Resolve the case when the active player has no card to play."""
    game_state.tricks_count += 1
    collector_deck = game_state.player_decks[opponent_player_index]
    _collect_pile(collector_deck, game_state.central_pile)

    if not game_state.player_decks[game_state.next_player_index]:
        return _game_result("finished", game_state)

    game_state.next_player_index = opponent_player_index
    game_state.penalty_remaining = 0
    game_state.payment_owner_index = None
    return None


def _handle_number_card(
    game_state: _GameState, opponent_player_index: int
) -> dict[str, str | int] | None:
    """Process a number card play in either regular or penalty mode."""
    if game_state.penalty_remaining:
        game_state.penalty_remaining -= 1
        if not game_state.penalty_remaining:
            game_state.tricks_count += 1
            assert game_state.payment_owner_index is not None
            collector_deck = game_state.player_decks[game_state.payment_owner_index]
            _collect_pile(collector_deck, game_state.central_pile)

            if not game_state.player_decks[0] or not game_state.player_decks[1]:
                return _game_result("finished", game_state)

            game_state.next_player_index = game_state.payment_owner_index
            game_state.payment_owner_index = None
        return None

    game_state.next_player_index = opponent_player_index
    return None


def _play_game(game_state: _GameState) -> dict[str, str | int]:
    """Play until the game finishes or a loop is detected."""
    observed_round_starts: set[tuple[tuple[str, ...], tuple[str, ...]]] = set()

    while True:
        if _start_of_round(game_state):
            if (
                round_signature := _loop_signature(game_state)
            ) in observed_round_starts:
                return _game_result("loop", game_state)
            observed_round_starts.add(round_signature)

        active_player_deck = game_state.player_decks[game_state.next_player_index]
        opponent_player_index = 1 - game_state.next_player_index

        if not active_player_deck:
            if finished_result := _handle_unable_to_play(
                game_state, opponent_player_index
            ):
                return finished_result
            continue

        played_card = active_player_deck.popleft()
        game_state.central_pile.append(played_card)
        game_state.played_cards_count += 1

        if (payment_value := PAYMENT_VALUES.get(played_card)) is not None:
            game_state.penalty_remaining = payment_value
            game_state.payment_owner_index = game_state.next_player_index
            game_state.next_player_index = opponent_player_index
            continue

        if finished_result := _handle_number_card(game_state, opponent_player_index):
            return finished_result


def simulate_game(player_a: list[str], player_b: list[str]) -> dict[str, str | int]:
    """Simulate a Camicia game and return status, played cards, and tricks."""
    game_state = _GameState([deque(player_a), deque(player_b)])
    return _play_game(game_state)
