from collections import Counter

# TODO: Handle punctuation and capitals


def get_frequency(word_string, word_to_count):
    res = 0
    for word in word_string.split(" "):
        if word == word_to_count:
            res += 1
    return res


def get_frequency_repeated(word_string, word_to_count):
    word_count = Counter(word_string.split(" "))
    print(word_count)
    return word_count[word_to_count]
