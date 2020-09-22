import unittest


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_sequences(bst):
    return bst_sequences_partial([], [bst])


def bst_sequences_partial(partial, subtrees):
    if not len(subtrees):
        return [partial]
    sequences = []
    for index, subtree in enumerate(subtrees):
        next_partial = partial + [subtree.val]
        next_subtrees = subtrees[:index] + subtrees[index + 1:]
        if subtree.left:
            next_subtrees.append(subtree.left)
        if subtree.right:
            next_subtrees.append(subtree.right)
        sequences += bst_sequences_partial(next_partial, next_subtrees)
    return sequences


class Test(unittest.TestCase):
    def test_bst_sequences(self):
        tree = Node(2, Node(1), Node(3))
        expected = [[2, 1, 3], [2, 3, 1]]
        self.assertEqual(expected, bst_sequences(tree))

        tree = Node(3, Node(2, Node(1)), Node(8))
        expected = [[3, 2, 8, 1], [3, 2, 1, 8], [3, 8, 2, 1]]
        self.assertEqual(expected, bst_sequences(tree))

        self.assertEqual(
            bst_sequences(Node(1, Node(8, Node(10)), Node(9))),
            [[1, 8, 9, 10], [1, 8, 10, 9], [1, 9, 8, 10]],
        )

        self.assertEqual(
            bst_sequences(Node(1, Node(8, Node(10), Node(6)), Node(9))),
            [
                [1, 8, 9, 10, 6],
                [1, 8, 9, 6, 10],
                [1, 8, 10, 9, 6],
                [1, 8, 10, 6, 9],
                [1, 8, 6, 9, 10],
                [1, 8, 6, 10, 9],
                [1, 9, 8, 10, 6],
                [1, 9, 8, 6, 10],
            ],
        )
