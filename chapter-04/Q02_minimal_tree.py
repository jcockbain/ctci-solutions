import unittest


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
        res = minimal_tree([1, 2, 3, 4, 5], 0, 4)
        self.assertEqual(3, res.val)
        self.assertEqual(1, res.left.val)
        self.assertEqual(2, res.left.right.val)
        self.assertEqual(4, res.right.val)
        self.assertEqual(5, res.right.right.val)
