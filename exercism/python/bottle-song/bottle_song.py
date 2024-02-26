def has_s(i: int) -> str:
    return "s" if i == 0 or i >= 2 else ""


def recite(start: int, take: int = 1) -> [str]:
    numbers = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    verse_template = ["{id} green bottle{s} hanging on the wall,",
                      "{id} green bottle{s} hanging on the wall,",
                      "And if one green bottle should accidentally fall,",
                      "There'll be {id_minus_one} green bottle{s} hanging on the wall."]

    song = []
    for i in range(start, start - take, -1):
        song.append(verse_template[0].format(id=numbers[i].capitalize(), s=has_s(i)))
        song.append(verse_template[1].format(id=numbers[i].capitalize(), s=has_s(i)))
        song.append(verse_template[2])
        song.append(verse_template[3].format(id_minus_one=numbers[i - 1], s=has_s(i - 1)))
        if take > 1:
            song.append("")

    if take > 1:
        song.pop()

    return song
