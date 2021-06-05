import random

PIECE_NOT_FOUND = [-1, -1]
NO_ONE_STARTS = "No one starts"
stock_pieces = list()


def init_stock_pieces():
    for up in range(0, 7):
        for down in range(0, 7):
            stock_pieces.append([up, down])
            if down == up:
                break


def get_random_pieces_from_stock(from_pieces: list, how_many_pieces: int) -> list:
    random_pieces = []
    random_elements = random.sample(range(len(from_pieces)), how_many_pieces)
    random_elements.sort(reverse=True)
    for i in random_elements:
        random_pieces.append(from_pieces.pop(i))
    return random_pieces


def is_double(piece: [int, int]) -> bool:
    return piece[0] == piece[1]


def find_highest_double(pieces: list) -> [int, int]:
    highest_double = PIECE_NOT_FOUND
    for piece in pieces:
        if is_double(piece) and piece[0] > highest_double[0]:
            highest_double = piece

    return highest_double


def starting_conditions(computer: list, player: list) -> ([int, int], str):
    highest_computer_piece = find_highest_double(computer)
    highest_player_piece = find_highest_double(player)

    if highest_computer_piece == highest_player_piece == PIECE_NOT_FOUND:
        return PIECE_NOT_FOUND, NO_ONE_STARTS, computer, player
    elif highest_computer_piece[0] > highest_player_piece[0]:
        computer.pop(computer.index(highest_computer_piece))
        return highest_computer_piece, "player", computer, player
    else:
        player.pop(player.index(highest_player_piece))
        return highest_player_piece, "computer", computer, player


def player_pieces_print(player: list) -> str:
    return "\n" + "".join([f"{i + 1}:{player[i]}\n" for i in range(len(player))])


def get_long_status(whose_next: str) -> str:
    if "player" == whose_next:
        return "It's your turn to make a move. Enter your command."
    else:
        return "Computer is about to make a move. Press Enter to continue..."


def print_game_state(all_pieces: list, computer: list, player: list, snake: [int, int], next_player: str):
    gui_width: int = 70
    print("=" * gui_width)
    print(f"Stock size: {len(all_pieces)}")
    print(f"Computer pieces: {len(computer)}")
    print(f"\n{snake}\n")
    print(f"Your pieces: {player_pieces_print(player)}")
    print(f"Status: {get_long_status(next_player)}")


init_stock_pieces()

computer_pieces = get_random_pieces_from_stock(stock_pieces, 7)
player_pieces = get_random_pieces_from_stock(stock_pieces, 7)
whose_next = NO_ONE_STARTS
domino_snake = PIECE_NOT_FOUND
circuit_breaker = 0
while whose_next == NO_ONE_STARTS and circuit_breaker < 10:
    domino_snake, whose_next, computer_pieces, player_pieces = starting_conditions(computer_pieces, player_pieces)
    circuit_breaker += 1
print_game_state(stock_pieces, computer_pieces, player_pieces, domino_snake, whose_next)
