import math
import random


class GameState:
    human_next = "Status: It's your turn to make a move. Enter your command."
    cpu_next = "Status: Computer is about to make a move. Press Enter to " \
               "continue... "
    human_won = "Status: The game is over. You won!"
    cpu_won = "Status: The game is over. The computer won!"
    draw = "Status: The game is over. It's a draw!"
    unknown = "Status: Unknown game state. Contact support 0700727272"
    end_game = [cpu_won, human_won, draw]


PIECE_NOT_FOUND = [-1, -1]
START_WITH_PIECES = 7
stock_pieces = []
computer_pieces = []
player_pieces = []
domino_snake = []
current_game_state = GameState.unknown


def init_stock_pieces() -> list[[int, int]]:
    all_dominoes = []
    for up in range(0, 7):
        for down in range(0, 7):
            all_dominoes.append([up, down])
            if down == up:
                break
    return all_dominoes


def get_random_pieces_from_stock(from_pieces: list,
                                 how_many_pieces: int) -> list:
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
        return PIECE_NOT_FOUND, GameState.unknown, computer, player
    elif highest_computer_piece[0] > highest_player_piece[0]:
        computer.pop(computer.index(highest_computer_piece))
        return highest_computer_piece, GameState.human_next, computer, player
    else:
        player.pop(player.index(highest_player_piece))
        return highest_player_piece, GameState.cpu_next, computer, player


def print_domino_snake():
    return "".join([f"[{piece[0]}, {piece[1]}]" for piece in domino_snake])


def print_player_pieces(player: list) -> str:
    return "\n" + "".join(
        [f"{i + 1}:{player[i]}\n" for i in range(len(player))])


def print_game_state(debug: bool):
    gui_width: int = 70
    print("=" * gui_width)
    if debug:
        print("==DEBUG===" * 7)
        print("=" * gui_width)
        print(f"Stock size: {stock_pieces}")
        print(f"Computer pieces: {computer_pieces}")

    else:
        print(f"Stock size: {len(stock_pieces)}")
        print(f"Computer pieces: {len(computer_pieces)}")

    if len(domino_snake) <= 6 or debug:
        print(f"\n{print_domino_snake()}\n")
    else:
        print(f"\n{domino_snake[0]}{domino_snake[1]}{domino_snake[2]}..."
              f"{domino_snake[-3]}{domino_snake[-2]}{domino_snake[-1]}\n")
    print(f"Your pieces: {print_player_pieces(player_pieces)}")
    print(f"{current_game_state}")


def init_game() -> GameState:
    game_state = GameState.unknown
    circuit_breaker = 0
    while current_game_state == GameState.unknown and circuit_breaker < 10:
        circuit_breaker += 1
        stock_pieces = init_stock_pieces()
        cpu_pieces = get_random_pieces_from_stock(stock_pieces, START_WITH_PIECES)
        human_pieces = get_random_pieces_from_stock(stock_pieces, START_WITH_PIECES)
        starting_piece, game_state, cpu_pieces, human_pieces = starting_conditions(
            cpu_pieces, human_pieces)
        domino_snake.clear()
        domino_snake.append(starting_piece)
    return game_state, stock_pieces, cpu_pieces, human_pieces


def cpu_makes_move() -> int:
    return random.randint(-len(computer_pieces), len(computer_pieces))


def numbers_used(look_for: int):
    used = 0
    for piece in domino_snake:
        if piece[0] == look_for:
            used += 1
        if piece[1] == look_for:
            used += 1
    return used


def check_for_stalemate() -> bool:
    head = domino_snake[0][0]
    tail = domino_snake[-1][1]
    if head == tail and numbers_used(head) == 8:
        True
    return False


def check_end_game_condition() -> GameState:
    if 0 == len(player_pieces):
        return GameState.human_won
    elif 0 == len(computer_pieces):
        return GameState.cpu_won
    elif check_for_stalemate():
        return GameState.draw
    return current_game_state


def is_move_valid(where: str, piece: [int, int]) -> bool:
    if "left" == where:
        if domino_snake[0][0] == piece[0] or domino_snake[0][0] == piece[1]:
            return True
    elif "right" == where:
        if domino_snake[-1][-1] == piece[0] or domino_snake[-1][-1] == piece[1]:
            return True
    else:
        print("[ERROR] Please provide where to match")

    return False


current_game_state, stock_pieces, computer_pieces, player_pieces = init_game()


def insert_piece(where: str, piece: [int, int]):
    if "left" == where:
        if domino_snake[0][0] == piece[1]:
            domino_snake.insert(0, piece)
        else:
            domino_snake.insert(0, [piece[1], piece[0]])
    elif "right" == where:
        if domino_snake[-1][-1] == piece[0]:
            domino_snake.append(piece)
        else:
            domino_snake.append([piece[1], piece[0]])


def check_int(s: str) -> bool:
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


while current_game_state not in GameState.end_game:
    current_game_state = check_end_game_condition()
    print_game_state(False)

    if current_game_state in GameState.end_game:
        exit(0)

    if GameState.human_next == current_game_state:
        player_input = input()
        if not check_int(player_input):
            print("Invalid input. Please try again.")
            continue
        player_input = int(player_input)
        if math.fabs(player_input) > len(player_pieces):
            print("Invalid input. Please try again.")
            continue
        if 0 == player_input:
            if 0 == len(stock_pieces):
                # print("There are no pieces left in stock! Turn skipped")
                continue
            else:
                player_pieces.append(get_random_pieces_from_stock(stock_pieces, 1).pop())
        elif player_input < 0:
            chosen_piece_index = int(math.fabs(player_input)) - 1
            if is_move_valid("left", player_pieces[chosen_piece_index]):
                insert_piece("left", player_pieces[chosen_piece_index])
            else:
                print("Illegal move. Please try again.")
                continue
            player_pieces.pop(chosen_piece_index)
        else:
            chosen_piece_index = int(math.fabs(player_input)) - 1
            if is_move_valid("right", player_pieces[chosen_piece_index]):
                insert_piece("right", player_pieces[chosen_piece_index])
            else:
                print("Illegal move. Please try again.")
                continue
            player_pieces.pop(chosen_piece_index)
        current_game_state = GameState.cpu_next
    elif GameState.cpu_next == current_game_state:
        # input()
        cpu_input = cpu_makes_move()
        if 0 == cpu_input:
            if 0 == len(stock_pieces):
                # print("There are no pieces left in stock! Turn skipped")
                continue
            else:
                computer_pieces.append(get_random_pieces_from_stock(stock_pieces, 1).pop())
        elif cpu_input < 0:
            chosen_piece_index = int(math.fabs(cpu_input)) - 1
            if is_move_valid("left", computer_pieces[chosen_piece_index]):
                insert_piece("left", computer_pieces[chosen_piece_index])
                computer_pieces.pop(chosen_piece_index)
            else:
                # print("Illegal move. Please try again.")
                continue
        else:
            chosen_piece_index = int(math.fabs(cpu_input)) - 1
            if is_move_valid("right", computer_pieces[chosen_piece_index]):
                insert_piece("right", computer_pieces[chosen_piece_index])
                computer_pieces.pop(chosen_piece_index)
            else:
                # print("Illegal move. Please try again.")
                continue
        current_game_state = GameState.human_next
