import unittest


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def partition(head, partition):
    lowerHead = None
    lowerEnd = None
    upperHead = None
    upperEnd = None

    while head:
        if head.val < partition:
            if not lowerHead:
                lowerHead = head
                lowerEnd = head
            else:
                lowerEnd.next = head
                lowerEnd = head
        else:
            if not upperHead:
                upperHead = head
                upperEnd = head
            else:
                upperEnd.next = head

        head = head.next

    lowerEnd.next = upperHead
    return lowerHead


class PartitionTest(unittest.TestCase):
    def test_partition(self):
        llHead = Node(1)
        llHead.next = Node(3)
        llHead.next.next = Node(2)
        llHead.next.next.next = Node(2)
        llHead.next.next.next.next = Node(4)

        expected = [1, 2, 2, 3, 4]
        result = partition(llHead, 3)
        self.assertEqual(1, llHead.val)
        self.assertEqual(2, llHead.next.val)
        self.assertEqual(2, llHead.next.next.val)
        self.assertEqual(3, llHead.next.next.next.val)
        self.assertEqual(4, llHead.next.next.next.next.val)
