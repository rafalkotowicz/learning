import os

YEAR_DIR = 'aoc_2023'
SOURCE_DIR = f'{YEAR_DIR}/src'
TESTS_DIR = f'{YEAR_DIR}/test'
RESOURCES_DIR = f'{TESTS_DIR}/resources'


def make_dirs() -> None:
    dirs: [str] = [YEAR_DIR, SOURCE_DIR, TESTS_DIR, RESOURCES_DIR]
    if any(os.path.exists(dir) for dir in dirs):
        raise RuntimeError('Directories already exists! Watch out to not overwrite your work!')
    else:
        os.makedirs(SOURCE_DIR)
        os.makedirs(TESTS_DIR)
        os.makedirs(RESOURCES_DIR)


def make_files(dir: str, prefix: str, suffix: str):
    for i in generate_01_to_25():
        with open(f'{dir}/{prefix}{i}{suffix}', 'w') as f:
            pass


def generate_01_to_25() -> [str]:
    result: [str] = []
    for i in range(1, 26):
        result.append(str(i).rjust(2, "0"))
    return result


def main():
    make_dirs()
    make_files(SOURCE_DIR, '_day', '.py')
    make_files(TESTS_DIR, 'test_day', '.py')
    make_files(RESOURCES_DIR, 'day', 'example.txt')
    make_files(RESOURCES_DIR, 'day', 'puzzle.txt')


if __name__ == "__main__":
    main()
