import unittest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word


def multi_search(string, words):
    trie = Trie()
    for word in words:
        trie.add_word(word)

    word_locations = {}

    for i in range(len(string)):
        node = trie.root
        idx = i
        while idx < len(string):
            c = string[idx]
            if c not in node.children:
                break
            node = node.children[c]
            if node.is_word:
                word = string[i : idx + 1]
                if word in word_locations:
                    word_locations[word].append(i)
                else:
                    word_locations[word] = [i]
            idx += 1
    return word_locations


class Test(unittest.TestCase):
    def test_trie(self):
        trie = Trie()
        trie.add_word("test")
        self.assertEqual(True, trie.search_word("test"))
        self.assertEqual(False, trie.search_word("testing"))

    def test_multi_search(self):
        test_string = "dogwalk"
        test_words = ["dog", "walk"]
        expected = {"dog": [0], "walk": [3]}
        self.assertEqual(expected, multi_search(test_string, test_words))

        test_string = "iamateststringiamlong"
        test_words = ["a", "i", "am", "test", "string", "long"]
        expected = {
            "i": [0, 11, 14],
            "a": [1, 3, 15],
            "am": [1, 15],
            "test": [4],
            "string": [8],
            "long": [17],
        }
        result = multi_search(test_string, test_words)
        self.assertEqual(expected, result)
