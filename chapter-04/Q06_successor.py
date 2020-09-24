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


def successor(node):
    if node.right:
        return get_leftmost(node.right)
    if node.parent and node.parent.val > node.val:
        return node.parent
    return None


def get_leftmost(node):
    if not node.left:
        return node
    return get_leftmost(node.left)


class Test(unittest.TestCase):
    def test_successor(self):
        self.assertEqual(successor(Node(2, Node(1))), None)
        self.assertEqual(successor(Node(2, Node(1), Node(3))).val, 3)
        self.assertEqual(successor(Node(3, Node(1), Node(5, Node(4)))).val, 4)
        self.assertEqual(successor(Node(2, Node(1), Node(3)).left).val, 2)
        self.assertEqual(successor(Node(2, Node(1), Node(3)).right), None)
