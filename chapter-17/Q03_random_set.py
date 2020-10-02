import unittest
import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def pick_random_set(nums, m, random_function=get_random):
    if m > len(nums):
        return None

    subset = nums[:m]

    for i in range(m, len(nums)):
        k = random_function(0, m)
        if k < m:
            subset[k] = nums[i]

    return subset


for _ in range(100):
    print(pick_random_set([1, 2, 3, 4, 5, 6, 7, 8], 4))


class Test(unittest.TestCase):
    def test_random_set(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual([8, 2, 3, 4], pick_random_set(arr, 4, lambda a, b: a))
        self.assertEqual(None, pick_random_set(arr, 10))

        for _ in range(100):
            subset = pick_random_set([1, 2, 3, 4, 5, 6, 7, 8], 4)
            self.assertEqual(4, len(subset))
