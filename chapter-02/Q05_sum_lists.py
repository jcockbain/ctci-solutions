import unittest

# TODO: follow-up


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def sum_lists(head1, head2):
    carry = 0
    res = Node(0)
    dummy = res
    while head1 or head2 or carry:
        val = carry

        if head1:
            val += head1.val
            head1 = head1.next

        if head2:
            val += head2.val
            head2 = head2.next

        carry = val // 10
        val = val % 10

        res.next = Node(val)
        res = res.next

    return dummy.next


class Test(unittest.TestCase):
    def test_sum_lists(self):
        list1 = Node(7, Node(1, Node(6, None)))
        list2 = Node(5, Node(9, Node(2, None)))
        output = sum_lists(list1, list2)

        self.assertEqual(2, output.val)
        self.assertEqual(1, output.next.val)
        self.assertEqual(9, output.next.next.val)

        list1 = Node(7, Node(1, Node(6, None)))
        list2 = Node(5, Node(9, Node(3, None)))
        output = sum_lists(list1, list2)

        self.assertEqual(2, output.val)
        self.assertEqual(1, output.next.val)
        self.assertEqual(0, output.next.next.val)
        self.assertEqual(1, output.next.next.next.val)
