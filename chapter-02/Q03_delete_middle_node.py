import unittest


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def delete_middle_node(node):
    node.val = node.next.val
    node.next = node.next.next


class Unittest(unittest.TestCase):
    def test_delete_middle_node(self):
        end = Node(4, None)
        middle = Node(2, end)
        head = Node(3, middle)
        delete_middle_node(middle)
        self.assertEqual(4, head.next.val)
        self.assertEqual(None, head.next.next)
