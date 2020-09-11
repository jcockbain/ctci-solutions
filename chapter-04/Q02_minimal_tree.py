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
