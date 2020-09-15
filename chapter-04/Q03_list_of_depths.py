import unittest
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_list_of_depths(root):
    res = []
    queue = deque([root])
    while queue:
        ll_node = LinkedListNode(0)
        ll_head = ll_node
        for _ in range(len(queue)):
            tree_node = queue.popleft()
            next_ll_node = LinkedListNode(tree_node.val)
            ll_node.next = next_ll_node
            ll_node = ll_node.next
            if tree_node.left:
                queue.append(tree_node.left)
            if tree_node.right:
                queue.append(tree_node.right)
        res.append(ll_head.next)
    return res


def get_ll_values(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


class Test(unittest.TestCase):
    def test_create_linked_list_of_depths(self):
        head = TreeNode(1)
        head.left = TreeNode(2)
        head.right = TreeNode(3)
        head.left.left = TreeNode(4)
        head.right.right = TreeNode(5)

        list_of_depths = create_list_of_depths(head)
        ll_values = [get_ll_values(head) for head in list_of_depths]
        self.assertEqual([1], ll_values[0])
        self.assertEqual([2, 3], ll_values[1])
        self.assertEqual([4, 5], ll_values[2])

