import unittest


def word_rectangle(words):
    word_list_by_length = group_words_by_length(words)
    max_word_length = max(word_list_by_length.keys())
    max_size = max_word_length * max_word_length
    tries = [None] * (max_word_length + 1)

    for size in range(max_size, 0, -1):
        for word_length in range(1, max_word_length):
            if word_length in word_list_by_length:
                word_list = word_list_by_length[word_length]
                if size % word_length == 0:
                    height = size / word_length
                    rectangle = make_rectangle(word_list, word_length, height, tries)
                    if rectangle:
                        return rectangle


def make_rectangle(words, length, height, tries):
    trie = tries[length]
    if not trie:
        tries[length] = Trie()
        trie = tries[length]
        for word in words:
            trie.add_word(word)

    def is_valid_rectangle(rectangles):
        for c in range(length):
            prefix = "".join([rectangles[r][c] for r in range(len(rectangles))])
            if not trie.is_valid_prefix(prefix):
                return False
        return True

    def backtrack(rectangles=[]):
        if not is_valid_rectangle(rectangles):
            return

        if len(rectangles) == height:
            return rectangles[:]

        for word in words:
            rectangles.append(word)
            res = backtrack(rectangles)
            if res:
                return res
            rectangles.pop()

    return backtrack()


def group_words_by_length(words):
    word_lengths = {}
    for word in words:
        word_length = len(word)
        if word_length not in word_lengths:
            word_lengths[word_length] = set([word])
        else:
            word_lengths[word_length].add(word)
    return word_lengths


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

    def is_valid_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


class Test(unittest.TestCase):
    def test_make_rectangle(self):
        words = [
            "grass",
            "rural",
            "argue",
            "sauce",
            "sleep",
            "pigeon",
            "pig",
            "camel",
            "bear",
            "dog",
        ]
        self.assertEqual(
            ["grass", "rural", "argue", "sauce", "sleep"], word_rectangle(words)
        )
