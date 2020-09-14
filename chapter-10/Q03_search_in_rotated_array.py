import unittest


def rotated_search(arr, target):
    return search(arr, target, 0, len(arr) - 1)


def search(nums, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    if nums[left] < nums[mid]:
        if nums[left] < target < nums[mid]:
            return search(nums, target, left, mid)
        else:
            return search(nums, target, mid + 1, right)
    elif nums[mid] < nums[right]:
        if nums[mid] < target < nums[right]:
            return search(nums, target, mid + 1, right)
        else:
            return search(nums, target, left, mid)

    else:
        location = -1

        if nums[left] == nums[mid]:
            location = search(nums, target, mid + 1, right)

        if location == -1 and nums[mid] == nums[right]:
            location = search(nums, target, left, mid - 1)

        return location


class RotatedSearchTest(unittest.TestCase):
    def test_rotated_search(self):
        array = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
        self.assertEqual(5, rotated_search(array, 1))

        array2 = [1, 2, 3, 4, 5]
        self.assertEqual(3, rotated_search(array2, 4))

        array3 = [5, 6, 7, 8, 1, 2, 3]
        self.assertEqual(2, rotated_search(array3, 7))

        array4 = [5, 5, 5, 6, 7, 8, 1, 2, 3]
        self.assertEqual(3, rotated_search(array4, 6))
