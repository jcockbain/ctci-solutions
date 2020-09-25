import unittest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminating = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.terminating = True

    def search(self, word):
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.terminating

    def starts_with(self, prefix):
        cur = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


letters = {
    1: "",
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: "",
}


def T9(code, words_trie):
    words_output = []

    def backtrack(idx=0, prefix=""):
        if idx == len(str(code)):
            if words_trie.search(prefix):
                words_output.append(prefix)
            return

        if not words_trie.starts_with(prefix):
            return

        number = int(str(code)[idx])

        for letter in letters[number]:
            backtrack(idx + 1, prefix + letter)

    backtrack()
    return words_output


class Test(unittest.TestCase):
    def test_t9(self):
        words = ["tree", "used", "been", "deer", "moon"]
        trie = Trie()
        for word in words:
            trie.add_word(word)
        self.assertEqual(["tree", "used"], T9(8733, trie))
        self.assertEqual(["moon"], T9(6666, trie))
