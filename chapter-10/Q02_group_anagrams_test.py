import unittest
from Q02_group_anagrams import group_anagrams


class GroupAnagramsTest(unittest.TestCase):
    def test_group_anagrams(self):
        wordList = ["cheese", "ham", "hceese", "mha", "spam"]
        expected = ["cheese", "hceese", "ham", "mha", "spam"]
        self.assertEqual(expected, group_anagrams(wordList))

        wordList2 = ["hello", "world", "olleh"]
        expected2 = ["hello", "olleh", "world"]
        self.assertEqual(expected2, group_anagrams(wordList2))
