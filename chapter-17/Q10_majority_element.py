import unittest


def majority_element(arr):
    num_elements = len(arr)
    count = 0
    element = 0

    for i in arr:
        if count == 0:
            element = i
        if i == element:
            count += 1
        else:
            count -= 1

    validate_count = 0
    for i in arr:
        if i == element:
            validate_count += 1

    return element if validate_count > num_elements / 2 else -1


class Test(unittest.TestCase):
    def test_majority_element(self):
        self.assertEqual(5, majority_element([1, 2, 5, 9, 5, 9, 5, 5, 5]))
        self.assertEqual(2, majority_element([2, 2, 2, 2, 2, 9, 5, 5, 5]))
        self.assertEqual(-1, majority_element([1, 2, 5, 9, 5, 9, 2, 3, 5]))
