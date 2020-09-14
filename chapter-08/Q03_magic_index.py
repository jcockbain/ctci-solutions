import unittest

# TODO : Follow up with duplicates


def find_magic_index(arr):  # O(N)
    for i in range(0, len(arr)):
        if arr[i] == i:
            return i
    return None


def find_magic_index_search(arr):  # O(log(N))
    min = 0
    max = len(arr) - 1
    return find_magic_index_2(arr, min, max)


def find_magic_index_2(arr, min, max):
    mid = int((min + max) / 2)
    if arr[mid] == mid:
        return mid
    if arr[mid] < mid:
        return find_magic_index_2(arr, mid + 1, max)
    if arr[mid] > mid:
        return find_magic_index_2(arr, min, mid - 1)


class Test(unittest.TestCase):
    def test_find_magic_index(self):
        self.assertEqual(find_magic_index([0, 1, 2, 3, 4]), 0)
        self.assertEqual(find_magic_index([1, 2, 3]), None)
        self.assertEqual(find_magic_index_search([0, 2, 3, 4]), 0)


if __name__ == "__main__":
    unittest.main()
