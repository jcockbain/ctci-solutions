import unittest
from LinkedList import LinkedListNode
from Q04_partition import partition
from LinkedListHelpers import print_list, get_list


class PartitionTest(unittest.TestCase):
    def test_partition(self):
        llHead = LinkedListNode(1)
        llHead.next = LinkedListNode(3)
        llHead.next.next = LinkedListNode(2)
        llHead.next.next.next = LinkedListNode(2)
        llHead.next.next.next.next = LinkedListNode(4)

        expected = [1, 2, 2, 3, 4]
        self.assertEqual(expected, get_list(partition(llHead, 3)))
