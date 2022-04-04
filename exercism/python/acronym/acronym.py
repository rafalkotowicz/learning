def abbreviate(words: str) -> str:
    abbreviated = ""
    for word in str.split(words, sep=" "):
        if word in ["-", ":"]:
            continue
        elif word.find("-") != -1:
            for subWord in str.split(word, sep="-"):
                abbreviated += find_first_alpha_upper(subWord)
        else:
            abbreviated += find_first_alpha_upper(word)

    return abbreviated


def find_first_alpha_upper(word: str) -> str:
    if word[0].isalpha():
        return word[0].upper()
    else:
        for character in list(word):
            if character.isalpha():
                return character
