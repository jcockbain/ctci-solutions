import unittest


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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
        root = TreeNode(1)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        self.assertTrue(check_balanced(root))

        root = TreeNode(1)
        root.left = TreeNode(4)
        root.left.left = TreeNode(5)
        self.assertFalse(check_balanced(root))
