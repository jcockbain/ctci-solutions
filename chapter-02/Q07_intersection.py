import unittest


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# solution 1 : using hashset


def intersection(list1, list2):
    seen = set()
    while list1:
        seen.add(list1)
        list1 = list1.next

    while list2:
        if list2 in seen:
            return list2
        list2 = list2.next


# solution 2 : constant space


def intersection_2(list_1, list_2):
    length_1 = get_linked_list_length(list_1)
    length_2 = get_linked_list_length(list_2)

    if length_1 > length_2:
        for _ in range(length_1 - length_2):
            list_1 = list_1.next
    else:
        for _ in range(length_2 - length_1):
            list_2 = list_2.next

    while list_1 and list_2:
        if list_1 == list_2:
            return list_1
        list_1 = list_1.next
        list_2 = list_2.next


def get_linked_list_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length


class Test(unittest.TestCase):
    def test_sum_lists(self):
        intersection_list = Node(7, Node(1, Node(1, Node(7, None))))
        intersection_list_1 = Node(2, intersection_list)
        intersection_list_2 = Node(3, Node(4, intersection_list))
        self.assertEqual(
            intersection_list, intersection(intersection_list_1, intersection_list_2)
        )

        non_intersection_list = Node(7)
        self.assertEqual(None, intersection(intersection_list, non_intersection_list))

        self.assertEqual(
            intersection_list, intersection_2(intersection_list_1, intersection_list_2)
        )

        non_intersection_list = Node(7)
        self.assertEqual(None, intersection_2(intersection_list, non_intersection_list))
