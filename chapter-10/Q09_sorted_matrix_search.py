import unittest

# TODO: Add binary search style solution


def sorted_matrix_search(matrix, target):
    m, n = len(matrix), len(matrix[0])
    r, c = 0, m - 1
    while r < m and c >= 0:
        if matrix[r][c] == target:
            return (r, c)
        elif matrix[r][c] > target:
            c -= 1
        else:
            r += 1


class Test(unittest.TestCase):
    def test_sorted_matrix_search(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual((1, 1), sorted_matrix_search(matrix, 5))
        self.assertEqual((2, 2), sorted_matrix_search(matrix, 9))
        self.assertEqual(None, sorted_matrix_search(matrix, 10))
