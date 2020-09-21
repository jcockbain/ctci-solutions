import unittest


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def detect_loop(head):
    seen = set()
    while head:
        if head in seen:
            return head
        seen.add(head)
        head = head.next


def detect_loop_2(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break

    if not fast or not fast.next:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast


class Test(unittest.TestCase):
    def test_sum_lists(self):
        looped_list = Node(7, Node(1, Node(1, Node(7, None))))
        looped_list.next = looped_list
        self.assertEqual(looped_list, detect_loop(looped_list))
        self.assertEqual(looped_list, detect_loop_2(looped_list))

        self.assertEqual(None, detect_loop(Node(7, Node(4, None))))
        self.assertEqual(None, detect_loop_2(Node(7, Node(4, None))))

        looped_list_2 = Node(1, Node(2, Node(3, looped_list)))
        self.assertEqual(looped_list, detect_loop(looped_list))
        self.assertEqual(looped_list, detect_loop_2(looped_list))
