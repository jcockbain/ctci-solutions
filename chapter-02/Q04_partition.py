import unittest
from LinkedList import LinkedListNode
from LinkedListHelpers import print_list, get_list


def partition(head, partition):
    lowerHead = None
    lowerEnd = None
    upperHead = None
    upperEnd = None

    while head:
        if head.value < partition:
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
        llHead = LinkedListNode(1)
        llHead.next = LinkedListNode(3)
        llHead.next.next = LinkedListNode(2)
        llHead.next.next.next = LinkedListNode(2)
        llHead.next.next.next.next = LinkedListNode(4)

        expected = [1, 2, 2, 3, 4]
        self.assertEqual(expected, get_list(partition(llHead, 3)))
