import unittest


def sum_swap(arr_1, arr_2):
    sum_1 = sum(arr_1)
    sum_2 = sum(arr_2)

    diff = sum_2 - sum_1

    # odd diffs have no solution
    if diff % 2 != 0:
        return []

    comp = {}
    for i in arr_1:
        comp[int(diff / 2) + i] = i

    for j in arr_2:
        if j in comp:
            return [comp[j], j]

    return []


class Test(unittest.TestCase):
    def test_sum_swap(self):
        self.assertEqual([1, 3], sum_swap([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]))
        self.assertEqual([3, 2], sum_swap([1, 2, 3, 4], [2, 3, 3]))
        self.assertEqual([], sum_swap([1, 2, 3, 4], [2, 3, 3, 1]))
        self.assertEqual([], sum_swap([1, 2, 3, 4], [2, 2, 1, 3, 4, 4, 2]))
