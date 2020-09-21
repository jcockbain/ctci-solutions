import unittest


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def kth_to_last(head, k):
    runner = current = head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current


class Test(unittest.TestCase):
    def test_kth_to_last(self):
        head = Node(1, Node(2, Node(1, Node(5, None))))
        self.assertEqual(5, kth_to_last(head, 1).val)
        self.assertEqual(1, kth_to_last(head, 2).val)
        self.assertEqual(2, kth_to_last(head, 3).val)
        self.assertEqual(1, kth_to_last(head, 4).val)

        self.assertEqual(None, kth_to_last(None, 1))
