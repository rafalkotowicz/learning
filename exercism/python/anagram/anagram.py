def is_anagram(word: str, candidate: str) -> bool:
    word = list(word.casefold())
    candidate = list(candidate.casefold())
    if word == candidate:
        return False
    return sorted(word) == sorted(candidate)


def find_anagrams(word: str, candidates: [str]) -> [str]:
    return [candidate for candidate in candidates if is_anagram(word, candidate)]
