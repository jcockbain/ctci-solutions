import unittest


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_subtree(t1, t2):
    t1_pre_order = pre_order_traversal(t1)
    t2_pre_order = pre_order_traversal(t2)
    return array_contains(t1_pre_order, t2_pre_order)


def array_contains(t1, t2):
    i2 = 0
    first_element = t2[i2]
    if first_element not in t1:
        return False

    i1 = t1.index(t2[0])
    while i2 < len(t2):
        if i1 >= len(t1) or t1[i1] != t2[i2]:
            return False
        i1 += 1
        i2 += 1
    return True


def pre_order_traversal(root):
    if not root:
        return [None]
    return [root.val] + pre_order_traversal(root.left) + pre_order_traversal(root.right)


class Test(unittest.TestCase):
    def test_check_subtree(self):
        t2 = Node(4, Node(5, Node(6)), Node(7))
        t1 = Node(1, Node(2, Node(3)), t2)
        self.assertEqual(True, check_subtree(t1, t2))

        t2 = Node(1, Node(3))
        t1 = Node(4, Node(5, Node(6)))
        self.assertEqual(False, check_subtree(t1, t2))

        t2 = Node(1, Node(3))
        t1 = Node(4, Node(5, Node(6, Node(1))))
        self.assertEqual(False, check_subtree(t1, t2))
