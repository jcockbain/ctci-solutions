import unittest


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def paths_with_sum(root, target):
    if not root:
        return 0
    new_target = target - root.val
    s = 1 if new_target == 0 else 0
    return (
        s
        + paths_with_sum(root.left, new_target)
        + paths_with_sum(root.right, new_target)
    )


class Test(unittest.TestCase):
    def test_paths_with_sum(self):
        root = Node(
            1,
            Node(2, Node(-1, Node(1), Node(3)), Node(3, Node(-2, Node(-1)), Node(-3))),
        )
        self.assertEqual(4, paths_with_sum(root, 3))

        root = Node(1, Node(2), Node(3))
        self.assertEqual(1, paths_with_sum(root, 3))
