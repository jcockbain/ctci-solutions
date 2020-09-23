import unittest


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root, target_sum):
    return pathSumRec(root, target_sum, [])


def pathSumRec(root, target_sum, currentPath):
    if root is None:
        return 0

    currentPath.append(root.val)
    pathCount, pathSum = 0, 0

    for i in range(len(currentPath) - 1, -1, -1):
        pathSum += currentPath[i]
        if pathSum == target_sum:
            pathCount += 1

    pathCount += pathSumRec(root.left, target_sum, currentPath)
    pathCount += pathSumRec(root.right, target_sum, currentPath)

    currentPath.pop()
    return pathCount


class Test(unittest.TestCase):
    def test_paths_with_sum(self):
        root = Node(
            1,
            Node(2, Node(-1, Node(1), Node(3)), Node(3, Node(-2, Node(-1)), Node(-3))),
        )
        self.assertEqual(7, pathSum(root, 3))

        root = Node(1, Node(2), Node(3))
        self.assertEqual(2, pathSum(root, 3))
