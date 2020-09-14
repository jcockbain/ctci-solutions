import unittest


def group_anagrams(word_list):
    anagrams = {}
    for w in word_list:
        sorted_word = "".join(sorted(w))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(w)
        else:
            anagrams[sorted_word] = [w]

    res = []
    for sorted_word in anagrams:
        for word in anagrams[sorted_word]:
            res.append(word)

    return res


class GroupAnagramsTest(unittest.TestCase):
    def test_group_anagrams(self):
        wordList = ["cheese", "ham", "hceese", "mha", "spam"]
        expected = ["cheese", "hceese", "ham", "mha", "spam"]
        self.assertEqual(expected, group_anagrams(wordList))

        wordList2 = ["hello", "world", "olleh"]
        expected2 = ["hello", "olleh", "world"]
        self.assertEqual(expected2, group_anagrams(wordList2))
