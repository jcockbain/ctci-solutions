import unittest
from Q02_minimal_tree import TreeNode, minimal_tree
from tree_helpers import in_order_traversal, level_order_traversal


class MinimalTreeTest(unittest.TestCase):
    def test_minimal_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.right = TreeNode(4)
        root.right.right = TreeNode(5)
        res = minimal_tree([1, 2, 3, 4, 5], 0, 4)
        self.assertEqual(level_order_traversal(root), level_order_traversal(res))

