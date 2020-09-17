import unittest


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def is_palindrome(head):
    fast = head
    slow = head

    stack = []

    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()

        if top != slow.val:
            return False

        slow = slow.next

    return True


class Test(unittest.TestCase):
    def test_sum_lists(self):
        list1 = Node(7, Node(1, Node(7, None)))
        self.assertEqual(True, is_palindrome(list1))

        list1 = Node(7, Node(1, Node(1, Node(7, None))))
        self.assertEqual(True, is_palindrome(list1))

        list1 = Node(7, Node(1, Node(6, None)))
        self.assertEqual(False, is_palindrome(list1))
