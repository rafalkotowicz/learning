"""Functions to automate Conda airlines ticketing system."""
import itertools
from typing import Generator, Any


def generate_seat_letters(number: int) -> Generator[str, Any, None]:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seats_letters: [str] = ["A", "B", "C", "D"]
    current_letter: int = 0
    while current_letter < number:
        yield seats_letters[current_letter % len(seats_letters)]
        current_letter += 1


def generate_seats(number: int) -> Generator[str, Any, None]:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    rows = (i for i in itertools.count(start=1) if i != 13 for _ in range(4))
    letters: Generator[str, Any, None] = generate_seat_letters(number)
    for row, letter in zip(rows, letters):
        yield str(row) + letter


def assign_seats(passengers: [str]) -> dict():
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(seat_numbers: [str], flight_id: str) -> Generator[str, Any, None]:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        yield (seat + flight_id).ljust(12, "0")
