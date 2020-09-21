import unittest


def sparse_search(strings, target):
    left = 0
    right = len(strings) - 1
    return binary_search(left, right, strings, target)


def binary_search(left, right, strings, target):
    if left > right:
        return -1

    mid = left + ((right - left) // 2)

    if strings[mid] == target:
        return mid

    elif strings[mid] == "":
        upper = mid + 1
        while upper <= right:
            if strings[upper] != "":
                if strings[upper] == target:
                    return upper
                elif strings[upper] > target:
                    return binary_search(left, mid - 1, strings, target)
                elif strings[upper] < target:
                    return binary_search(upper + 1, right, strings, target)
            upper += 1

        lower = mid - 1
        while lower >= left:
            if strings[lower] != "":
                if strings[lower] == target:
                    return lower
                elif strings[lower] > target:
                    return binary_search(left, lower - 1, strings, target)
                elif strings[upper] < target:
                    return binary_search(mid + 1, right, strings, target)
            lower -= 1

    elif strings[mid] > target:
        return binary_search(left, mid - 1, strings, target)

    elif strings[mid] < target:
        return binary_search(mid + 1, right, strings, target)

    return -1


class Test(unittest.TestCase):
    def test_power_of_two(self):
        self.assertEqual(
            3, sparse_search(["at", "", "", "ball", "", "", "", "cat"], "ball")
        )
        self.assertEqual(
            1, sparse_search(["at", "ball", "", "", "", "", "", ""], "ball")
        )
        self.assertEqual(
            0, sparse_search(["at", "", "back", "", "ball", "", "", "cat"], "at")
        )
        self.assertEqual(
            7, sparse_search(["at", "", "", "", "ball", "", "", "cat"], "cat")
        )
        self.assertEqual(
            -1, sparse_search(["at", "", "", "", "ball", "", "", "cat"], "hat")
        )
        self.assertEqual(
            -1, sparse_search(["at", "", "back", "", "ball", "", "", ""], "hat")
        )
        self.assertEqual(
            -1, sparse_search(["", "", "back", "", "ball", "", "", ""], "at")
        )
        self.assertEqual(
            6,
            sparse_search(
                ["at", "bat", "cat", "gate", "mate", "pat", "sat", "yak"], "sat"
            ),
        )

