"""Core game logic for the Exercism Hangman exercise."""

# Game status categories
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    """Track the game state for a single hangman word."""

    def __init__(self, word: str) -> None:
        """Initialize a game with a target word and 9 allowed failures."""
        self.word = word
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.guessed_letters: set[str] = set()

    def guess(self, char: str) -> None:
        """Apply one guessed character and update game status."""
        if self.status != STATUS_ONGOING:
            raise ValueError('The game has already ended.')

        is_new_guess = char not in self.guessed_letters
        self.guessed_letters.add(char)

        if (not is_new_guess) or (char not in self.word):
            self.remaining_guesses -= 1

        if self.get_masked_word() == self.word:
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self) -> str:
        """Return the word with unknown letters replaced by underscores."""
        return ''.join(
            letter if letter in self.guessed_letters else '_'
            for letter in self.word
        )

    def get_status(self) -> str:
        """Return current game status: ongoing, win, or lose."""
        return self.status
