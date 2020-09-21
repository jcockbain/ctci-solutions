import unittest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_balanced(root):
    def is_balanced(root):
        if not root:
            return True, -1

        leftIsBalanced, leftHeight = is_balanced(root.left)
        if not leftIsBalanced:
            return False, 0

        rightIsBalanced, rightHeight = is_balanced(root.right)
        if not rightIsBalanced:
            return False, 0

        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)

    return is_balanced(root)[0]


class Test(unittest.TestCase):
    def test_check_balanced(self):
        bal_tree = TreeNode(1, TreeNode(4), TreeNode(5))
        self.assertTrue(check_balanced(bal_tree))

        unbal_tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        self.assertFalse(check_balanced(unbal_tree))

        unbal_tree = TreeNode(
            1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4)))
        )
        self.assertFalse(check_balanced(unbal_tree))

