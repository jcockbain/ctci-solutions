import unittest


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def validate_bst(root):
    if not root:
        return True

    stack = [(root, float("-inf"), float("inf"))]
    while stack:
        root, lower, upper = stack.pop()
        if not root:
            continue
        val = root.val
        if val <= lower or val >= upper:
            return False
        stack.append((root.right, val, upper))
        stack.append((root.left, lower, val))
    return True


class Test(unittest.TestCase):
    def test_check_balanced(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.right = TreeNode(4)
        self.assertTrue(validate_bst(root))

        root = TreeNode(2)
        root.left = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertFalse(validate_bst(root))
