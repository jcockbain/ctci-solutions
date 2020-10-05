import unittest
import heapq


class ContinuousMedian:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def add(self, n):
        if not self.maxHeap or -self.maxHeap[0] >= n:
            heapq.heappush(self.maxHeap, -n)
        else:
            heapq.heappush(self.minHeap, n)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def get_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
        return -self.maxHeap[0] / 1.0


class Test(unittest.TestCase):
    def test_volume_of_histogram(self):
        median_tracker = ContinuousMedian()
        median_tracker.add(1)
        self.assertEqual(1, median_tracker.get_median())

        median_tracker.add(2)
        median_tracker.add(3)
        self.assertEqual(2, median_tracker.get_median())

        median_tracker.add(1)
        self.assertEqual(1.5, median_tracker.get_median())
