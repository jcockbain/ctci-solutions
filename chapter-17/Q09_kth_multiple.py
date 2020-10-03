import unittest
import heapq


def kth_multiple(n):
    val = 1
    elements = [1, 3, 5, 7]

    for i in range(n):
        min_element = heapq.heappop(elements)
        while elements[0] == min_element:
            heapq.heappop(elements)
        for x in [3, 5, 7]:
            heapq.heappush(elements, min_element * x)
    return min_element


class Test(unittest.TestCase):
    def test_kth_multiple(self):
        self.assertEqual(3, kth_multiple(2))
        self.assertEqual(7, kth_multiple(4))
        self.assertEqual(15, kth_multiple(6))
        self.assertEqual(25, kth_multiple(8))
        self.assertEqual(45, kth_multiple(11))
