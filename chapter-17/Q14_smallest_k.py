import unittest
import heapq


def smallest_k(nums, k):
    heapq.heapify(nums)
    res = []
    for _ in range(k):
        res.append(heapq.heappop(nums))
    return res


class Test(unittest.TestCase):
    def test_smallest_k(self):
        self.assertEqual([1, 2, 3], smallest_k([1, 2, 3, 4, 5], 3))
        self.assertEqual([1, 2], smallest_k([1, 2, 3, 4, 5], 2))
