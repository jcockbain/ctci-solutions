import unittest

# assuming elements can be reused


def pairs_with_sum(arr, target):
    counter = {}
    res = []
    for num in arr:
        if target - num in counter:
            for _ in range(counter[target - num]):
                res.append((target - num, num))
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    return res


class Test(unittest.TestCase):
    def test_pairs_with_sum(self):
        arr = [2, 3, 5, 1, 4]
        self.assertEqual([(2, 3), (1, 4)], pairs_with_sum(arr, 5))
        self.assertEqual([(3, 5)], pairs_with_sum(arr, 8))
        self.assertEqual([], pairs_with_sum(arr, 1))

        arr = [2, 2, 3]
        self.assertEqual([(2, 3), (2, 3)], pairs_with_sum(arr, 5))
