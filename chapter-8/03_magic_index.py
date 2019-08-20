import unittest


def test_find_magic_index(arr):  # O(N)
    for i in range(0, len(arr)):
        if arr[i] == i:
            return i
    return None


def test_find_magic_index_search(arr):
    min = 0
    max = len(arr) - 1
    return test_find_magic_index_2(arr, min, max)


def test_find_magic_index_2(arr, min, max):  # O(log(N))
    mid = int((min + max) / 2)
    if arr[mid] == mid:
        return mid
    if arr[mid] < mid:
        return test_find_magic_index_2(arr, mid + 1, max)
    if arr[mid] > mid:
        return test_find_magic_index_2(arr, min, mid - 1)


class Test(unittest.TestCase):
    def test_find_magic_index(self):
        self.assertEqual(test_find_magic_index([0, 1, 2, 3, 4]), 0)
        self.assertEqual(test_find_magic_index([1, 2, 3]), None)
        self.assertEqual(test_find_magic_index_search([0, 0, 1, 2, 3]), 0)
        self.assertEqual(test_find_magic_index_search([1, 1, 2, 3]), 1)
        self.assertEqual(test_find_magic_index_search([1, 1, 2, 3]), 1)


if __name__ == "__main__":
    unittest.main()
