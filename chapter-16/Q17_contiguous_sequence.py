import unittest


def contiguous_sequence(nums):
    max_sum = 0
    current_sum = 0

    for i in nums:
        current_sum += i
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum


class Test(unittest.TestCase):
    def test_contiguous_sequence(self):
        self.assertEqual(5, contiguous_sequence([2, -8, 3, -2, 4, -10]))
        self.assertEqual(20, contiguous_sequence([2, 6, 12]))
        self.assertEqual(0, contiguous_sequence([-3, -8, -10, -1]))
