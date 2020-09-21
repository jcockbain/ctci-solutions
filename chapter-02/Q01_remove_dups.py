import unittest


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def remove_dups(head):
    if head is None:
        return head

    current = head
    seen = set([current.val])
    while current.next:
        if current.next.val in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.val)
            current = current.next
    return head


def remove_dups_followup(head):
    if head is None:
        return head

    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return head


class Test(unittest.TestCase):
    def test_remove_dups(self):
        head = Node(1, Node(2, Node(1, Node(5, None))))
        remove_dups(head)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 2)
        self.assertEqual(head.next.next.val, 5)

        head = Node(1, Node(2, Node(1, Node(5, None))))
        remove_dups_followup(head)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 2)
        self.assertEqual(head.next.next.val, 5)

        self.assertEqual(None, remove_dups(None))
        self.assertEqual(None, remove_dups_followup(None))
