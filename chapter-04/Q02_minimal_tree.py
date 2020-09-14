import unittest
from tree_helpers import in_order_traversal, level_order_traversal


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def minimal_tree(nums, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = TreeNode(nums[mid])
    root.left = minimal_tree(nums, start, mid - 1)
    root.right = minimal_tree(nums, mid + 1, end)
    return root


class MinimalTreeTest(unittest.TestCase):
    def test_minimal_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.right = TreeNode(4)
        root.right.right = TreeNode(5)
        res = minimal_tree([1, 2, 3, 4, 5], 0, 4)
        self.assertEqual(level_order_traversal(root), level_order_traversal(res))
