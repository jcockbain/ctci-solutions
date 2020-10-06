from collections import defaultdict, deque
import unittest

# TODO: Implement bidirectional BFS solution


def recreate_path(beginWord, endWord, previous_node):
    node = endWord
    res = []
    while node is not beginWord:
        if node not in previous_node:
            return []
        res.append(node)
        node = previous_node[node]
    return [beginWord] + res[::-1]


def word_transformer(beginWord, endWord, wordList):
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return []

    L = len(beginWord)
    graph = defaultdict(list)

    for word in wordList:
        for i in range(L):
            graph[word[:i] + "*" + word[i + 1 :]].append(word)

    queue = deque([beginWord])
    previous_word = {}

    while queue:
        current_word = queue.popleft()
        for i in range(L):
            intermediate_word = current_word[:i] + "*" + current_word[i + 1 :]
            for word in graph[intermediate_word]:
                if word == endWord:
                    previous_word[word] = current_word
                    return recreate_path(beginWord, endWord, previous_word)
                if word not in previous_word:
                    previous_word[word] = current_word
                    queue.append(word)

            graph[intermediate_word] = []

    return []


class Test(unittest.TestCase):
    def test_recreate_path(self):
        previous_node = {"hit": "hot", "hot": "not"}
        self.assertEqual(
            ["not", "hot", "hit"], recreate_path("not", "hit", previous_node)
        )
        self.assertEqual([], recreate_path("got", "hot", previous_node))

    def test_word_transformer(self):
        words = ["hot", "dot", "dog", "lot", "log", "cog", "hit"]
        start = "hit"
        end = "cog"
        expected = ["hit", "hot", "dot", "dog", "cog"]
        self.assertEqual(expected, word_transformer(start, end, words))

        words = ["hot", "dog", "dot", "log", "lot"]
        start = "hit"
        end = "cog"
        expected = ["hit", "hot", "dot", "dog", "cog"]
        self.assertEqual([], word_transformer(start, end, words))

        words = ["big", "rig", "rid", "lid", "lad", "bad"]
        start = "bad"
        end = "big"
        expected = ["bad", "lad", "lid", "rid", "rig", "big"]
        self.assertEqual(expected, word_transformer(start, end, words))

        words = ["bad", "lad", "lid", "rid", "rig", "big", "bop"]
        start = "bad"
        end = "bop"
        expected = []
        self.assertEqual(expected, word_transformer(start, end, words))
