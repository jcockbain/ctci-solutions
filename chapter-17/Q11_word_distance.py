import unittest

# for single call


def word_distance(words, word_1, word_2):
    n = len(words)
    current_1, current_2 = None, None
    min_diff = float("inf")

    for i in range(n):
        if words[i] == word_1:
            current_1 = i
            if current_2:
                min_diff = min(min_diff, abs(current_2 - current_1))
        elif words[i] == word_2:
            current_2 = i
            if current_1:
                min_diff = min(min_diff, abs(current_2 - current_1))
    return min_diff


# for lots of repeated calls


class WordDistance:
    def __init__(self, words):
        self.word_positions = {}
        self.add_words(words)

    def add_words(self, words):
        n = len(words)

        for i in range(n):
            word = words[i]
            if word in self.word_positions:
                self.word_positions[word].append(i)
            else:
                self.word_positions[word] = [i]

    def get_distance(self, word_1, word_2):
        positions_1 = self.word_positions[word_1]
        positions_2 = self.word_positions[word_2]

        idx_1, idx_2 = 0, 0
        min_diff = float("inf")

        while idx_1 < len(positions_1) and idx_2 < len(positions_2):
            diff = positions_1[idx_1] - positions_2[idx_2]
            min_diff = min(min_diff, abs(diff))
            if diff > 0:
                idx_2 += 1
            else:
                idx_1 += 1
        return min_diff


class Test(unittest.TestCase):
    def test_word_distance(self):
        words = [
            "camel",
            "lion",
            "goat",
            "llama",
            "squirrel",
            "tiger",
            "monkey",
            "elephant",
            "camel",
        ]

        self.assertEqual(4, word_distance(words, "camel", "squirrel"))
        self.assertEqual(1, word_distance(words, "squirrel", "tiger"))
        self.assertEqual(2, word_distance(words, "lion", "llama"))

        wordDistance = WordDistance(words)
        self.assertEqual(4, wordDistance.get_distance("camel", "squirrel"))
        self.assertEqual(1, wordDistance.get_distance("squirrel", "tiger"))
        self.assertEqual(2, wordDistance.get_distance("lion", "llama"))
