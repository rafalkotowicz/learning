"""Food Chain exercise implementation."""

ANIMALS = (
    "fly",
    "spider",
    "bird",
    "cat",
    "dog",
    "goat",
    "cow",
    "horse",
)

REMARK_BY_ANIMAL = {
    "spider": "It wriggled and jiggled and tickled inside her.",
    "bird": "How absurd to swallow a bird!",
    "cat": "Imagine that, to swallow a cat!",
    "dog": "What a hog, to swallow a dog!",
    "goat": "Just opened her throat and swallowed a goat!",
    "cow": "I don't know how she swallowed a cow!",
    "horse": "She's dead, of course!",
}

FINAL_FLY_LINE = "I don't know why she swallowed the fly. Perhaps she'll die."
SPIDER_ANIMAL = "spider"
HORSE_ANIMAL = "horse"
SPIDER_TARGET = "spider that wriggled and jiggled and tickled inside her"


def _animal_phrase_for_target(animal):
    """Return target phrase used in 'to catch ...' lines."""
    if animal == SPIDER_ANIMAL:
        return SPIDER_TARGET
    return animal


def _build_verse(verse_number):
    """Build a single verse as a list of lines."""
    animal = ANIMALS[verse_number - 1]
    lines = [f"I know an old lady who swallowed a {animal}."]

    if remark := REMARK_BY_ANIMAL.get(animal):
        lines.append(remark)

    if animal == HORSE_ANIMAL:
        return lines

    for index in range(verse_number - 1, 0, -1):
        predator = ANIMALS[index]
        prey = _animal_phrase_for_target(ANIMALS[index - 1])
        lines.append(f"She swallowed the {predator} to catch the {prey}.")

    lines.append(FINAL_FLY_LINE)
    return lines


def recite(start_verse, end_verse):
    """Return verses from start_verse to end_verse as song lines."""
    song_lines = []

    for verse_number in range(start_verse, end_verse + 1):
        if song_lines:
            song_lines.append("")
        song_lines.extend(_build_verse(verse_number))

    return song_lines
