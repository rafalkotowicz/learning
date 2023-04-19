def translate(text: str) -> str:
    words: [str] = text.split()
    result: str = ""

    for word in words:
        result += translate_word(word) + " "

    return result.strip()


def translate_word(word: str) -> str:
    if is_rule_1_vowel(word):
        return f"{word}ay"

    is_rule_2_triggered, consonant_length = is_rule_2_consonant(word)
    if is_rule_2_triggered:
        if is_rule_3(word, consonant_length):
            return f"{word[consonant_length + 2:]}{word[0:consonant_length + 2]}ay"
        if is_rule_4(word, consonant_length):
            pass
        return f"{word[consonant_length:]}{word[0:consonant_length]}ay"

    return "Cannot Translate"


def is_rule_1_vowel(text: str) -> bool:
    sound_like_vowel: [str] = ["xr", "yt"]
    vovels: [str] = ["a", "e", "i", "o", "u"]
    vowel_sounds: [str] = []
    vowel_sounds.extend(sound_like_vowel)
    vowel_sounds.extend(vovels)

    for vowel_sound in vowel_sounds:
        if text.startswith(vowel_sound):
            return True

    return False


def is_rule_2_consonant(text: str) -> (bool, int):
    consonant_clusters: [str] = ["sch", "thr", "ch", "th", "xr", "qu", "rh"]
    consonants: [str] = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t",
                         "v", "w", "x", "y", "z"]
    consonant_sounds: [str] = []
    consonant_sounds.extend(consonant_clusters)
    consonant_sounds.extend(consonants)

    for consonant in consonant_sounds:
        if text.startswith(consonant):
            return True, len(consonant)

    return False, -1


def is_rule_3(text: str, consonant_length: int) -> bool:
    start: int = consonant_length
    end: int = consonant_length + len("qu")
    return text.find("qu", start, end) != -1


def is_rule_4(text: str, consonant_length: int) -> bool:
    start: int = consonant_length
    end: int = consonant_length + len("y")
    return text.find("y", start, end) != -1
