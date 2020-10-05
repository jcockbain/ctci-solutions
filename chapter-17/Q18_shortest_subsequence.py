import unittest
from collections import defaultdict


def shortest_subsequence(short, long):
    len_shortest = float("inf")
    current_shortest = None
    list_of_indices = {}

    for i in range(len(long)):
        end, elements = i, set(short)
        while end < len(long) and elements:
            x = long[end]
            if x in elements:
                elements.remove(long[end])
            end += 1
        if not elements and end - i < len_shortest:
            len_shortest = end - i
            current_shortest = [i, end - 1]
    return current_shortest


# TODO: O(B) solution


class Test(unittest.TestCase):
    def test_shortest_subsequence(self):
        short = [1, 5, 9]
        long = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
        self.assertEqual([7, 10], shortest_subsequence(short, long))

        short = [7, 5, 2]
        long = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
        self.assertEqual([0, 4], shortest_subsequence(short, long))

        short = [9, 1, 7]
        long = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
        self.assertEqual([8, 10], shortest_subsequence(short, long))

