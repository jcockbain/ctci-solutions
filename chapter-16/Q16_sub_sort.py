import unittest


def sub_sort(nums):
    target = sorted(nums)
    min_diff = float("inf")
    min_idxs = None
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if j - i < min_diff:
                sub_sorted = nums[:i] + sorted(nums[i : j + 1]) + nums[j + 1 :]
                if sub_sorted == target:
                    min_diff = j - i
                    min_idxs = (i, j)
    return min_idxs


class Test(unittest.TestCase):
    def test_sub_sort(self):
        self.assertEqual(
            (3, 9), sub_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
        )
