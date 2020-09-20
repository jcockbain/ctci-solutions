import unittest


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


def first_common_ancestor(node_1, node_2):
    parents_1, parents_2 = {}, {}
    while node_1 or node_2:
        if node_1:
            if node_1 in parents_2:
                return node_1
            parents_1[node_1] = True
            node_1 = node_1.parent
        if node_2:
            if node_2 in parents_1:
                return node_2
            parents_2[node_2] = True
            node_2 = node_2.parent
    return None


class Test(unittest.TestCase):
    def test_first_common_ancestor(self):
        node_1 = Node(1, Node(2), Node(3))
        node_2 = Node(2)
        ancestor = Node(2, node_1, Node(4, node_2))
        root = Node(1, Node(2, ancestor))
        self.assertEqual(ancestor, first_common_ancestor(node_1, node_2))
