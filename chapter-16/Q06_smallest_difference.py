import unittest


def smallest_difference(nums_1, nums_2):

    nums_1.sort()
    nums_2.sort()

    idx_1, idx_2 = 0, 0
    min_diff = float("inf")

    while idx_1 < len(nums_1) and idx_2 < len(nums_2):
        diff = nums_1[idx_1] - nums_2[idx_2]
        min_diff = min(min_diff, abs(diff))
        if diff > 0:
            idx_2 += 1
        else:
            idx_1 += 1
    return min_diff


class Test(unittest.TestCase):
    def test_trailing_zeroes(self):
        nums_1 = [1, 3, 15, 11, 2]
        nums_2 = [23, 127, 235, 19, 8]
        self.assertEqual(3, smallest_difference(nums_1, nums_2))

        nums_1 = [1, 3, 10]
        nums_2 = [12, 15]
        self.assertEqual(2, smallest_difference(nums_1, nums_2))

        nums_1 = [1, 3, 7, 8, 11]
        nums_2 = [5, 12]
        self.assertEqual(1, smallest_difference(nums_1, nums_2))
