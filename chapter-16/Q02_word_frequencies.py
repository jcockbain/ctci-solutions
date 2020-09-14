import unittest
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
    return word_count[word_to_count]


class WordFrequenciesTest(unittest.TestCase):
    def test_word_frequencies(self):
        test_string = "hello world, i just wanted to say hello"
        self.assertEqual(2, get_frequency(test_string, "hello"))
        self.assertEqual(2, get_frequency_repeated(test_string, "hello"))

