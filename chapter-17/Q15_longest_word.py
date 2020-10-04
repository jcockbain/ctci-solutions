import unittest


def longest_word(words):
    words.sort(reverse=True, key=lambda x: len(x))
    for word in words:
        dp = [None] * len(word)
        if can_be_split(word, 0, True, words, dp):
            return word


def can_be_split(word, idx, is_original_word, words, dp):
    if idx == len(word):
        return not is_original_word

    is_valid_split = False
    if dp[idx] is None:
        for end in range(idx, len(word) + 1):
            if word[idx:end] in words and can_be_split(word, end, False, words, dp):
                is_valid_split = True
                break
        dp[idx] = is_valid_split

    return dp[idx]


class Test(unittest.TestCase):
    def test_loongest_word(self):
        self.assertEqual(
            "dogwalker",
            longest_word(
                ["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"]
            ),
        )
        self.assertEqual(
            "dogwalk",
            longest_word(["cat", "banana", "dog", "nana", "walk", "dogwalk"]),
        )
