import re


class Game:

    def __init__(self, id: int, red: [int], green: [int], blue: [int]):
        self.game_id: int = id
        self.red_cubes: [int] = red
        self.green_cubes: [int] = green
        self.blue_cubes: [int] = blue


def find_game_prefix(line: str) -> str:
    return re.match(r'Game [0-9]+:', line).group()


def extract_game_id(game_prefix: str) -> int:
    return int(re.search(r'[0-9]+', game_prefix).group())


def remove_game_prefix(line: str) -> str:
    return re.sub(r'Game [0-9]+: ', '', line)


def combine_turns(line: str) -> str:
    return line.replace(';', ',')


def possible_games(lines: [str], red_max: int, green_max: int, blue_max: int) -> int:
    games: [Game] = []

    for line in lines:
        red_cubes = []
        green_cubes = []
        blue_cubes = []
        game_id = extract_game_id(find_game_prefix(line))
        line = remove_game_prefix(line)
        line = combine_turns(line)
        elf_grabs = line.split(",")
        for grab in elf_grabs:
            count, color = grab.strip().split(" ")
            if color == "red":
                red_cubes.append(int(count))
            if color == "green":
                green_cubes.append(int(count))
            if color == "blue":
                blue_cubes.append(int(count))
        games.append(Game(game_id, red_cubes, green_cubes, blue_cubes))

    sum_of_possible = 0
    for game in games:
        if max(game.red_cubes) <= red_max and max(game.green_cubes) <= green_max and max(game.blue_cubes) <= blue_max:
            sum_of_possible = sum_of_possible + game.game_id

    return sum_of_possible


def possible_games_2(lines: [str]) -> int:
    games: [Game] = []

    for line in lines:
        red_cubes = []
        green_cubes = []
        blue_cubes = []
        game_id = extract_game_id(find_game_prefix(line))
        line = remove_game_prefix(line)
        line = combine_turns(line)
        elf_grabs = line.split(",")
        for grab in elf_grabs:
            count, color = grab.strip().split(" ")
            if color == "red":
                red_cubes.append(int(count))
            if color == "green":
                green_cubes.append(int(count))
            if color == "blue":
                blue_cubes.append(int(count))
        games.append(Game(game_id, red_cubes, green_cubes, blue_cubes))

    sum_of_possible = 0
    for game in games:
        sum_of_possible += max(game.red_cubes) * max(game.green_cubes) * max(game.blue_cubes)

    return sum_of_possible
