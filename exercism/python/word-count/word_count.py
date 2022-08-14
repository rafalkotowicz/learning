def count_words(sentence: str) -> {}:
    sentence = sentence.lower() \
        .replace(",", " ") \
        .replace(".", " ") \
        .replace(":", " ") \
        .replace("!", " ") \
        .replace("&", " ") \
        .replace("@", " ") \
        .replace("$", " ") \
        .replace("%", " ") \
        .replace("^", " ") \
        .replace("_", " ") \
        .replace("\n", " ")

    words_in_sentence = sentence.split()

    words = dict()
    for word in words_in_sentence:
        while (word.find("'") != -1):
            if word[0] == "'":
                word = word[1::]
            elif word[-1] == "'":
                word = word[:-1:]
            else:
                break

        if word.strip() == "":
            continue

        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

    return words
