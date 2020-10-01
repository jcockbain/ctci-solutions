import unittest


def letters_and_numbers(arr):
    binary_arr = convert(arr)

    diff = 0
    first_idx_with_tracker_value = {0: 0}
    max_idx_pair = (0, 0)
    max_arr_length = 0
    for i, x in enumerate(binary_arr):
        if x:
            diff += 1
        else:
            diff -= 1
        if diff in first_idx_with_tracker_value:
            pair_idx = first_idx_with_tracker_value[diff]
            if i - pair_idx > max_arr_length:
                max_arr_length = i - pair_idx
                max_idx_pair = (pair_idx, i)
        else:
            first_idx_with_tracker_value[diff] = i + 1
    return arr[max_idx_pair[0] : max_idx_pair[1] + 1]


def convert(arr):
    res = [None] * len(arr)
    for i, x in enumerate(arr):
        if x.isalpha():
            res[i] = 1
        elif x.isnumeric():
            res[i] = 0
    return res


class Test(unittest.TestCase):
    def test_convert(self):
        arr = ["1", "a", "2", "3", "b", "c", "2", "1"]
        self.assertEqual([0, 1, 0, 0, 1, 1, 0, 0], convert(arr))

    def test_letters_and_numbers(self):
        arr = ["1", "a", "2", "3", "b", "c", "2", "1"]
        self.assertEqual(["1", "a", "2", "3", "b", "c"], letters_and_numbers(arr))

        arr = ["b", "a", "2", "3", "b", "c", "2", "1"]
        self.assertEqual(arr, letters_and_numbers(arr))

        arr = ["a", "b", "c", "1", "1", "b", "2", "c"]
        self.assertEqual(["b", "c", "1", "1", "b", "2",], letters_and_numbers(arr))
