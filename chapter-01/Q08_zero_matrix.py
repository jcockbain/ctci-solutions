import unittest

# TODO: O(1) space solution


def zero_matrix(matrix):
    h, w = len(matrix), len(matrix[0])
    zero_rows = [0] * h
    zero_cols = [0] * w

    for r in range(h):
        for c in range(w):
            if matrix[r][c] == 0:
                zero_rows[r] = 1
                zero_cols[c] = 1

    for r in range(h):
        for c in range(w):
            if zero_rows[r] or zero_cols[c]:
                matrix[r][c] = 0


class Test(unittest.TestCase):
    def test_zero_marix(self):
        matrix = [
            [1, 0, 3],
            [4, 5, 6],
            [7, 8, 0],
        ]
        expected = [
            [0, 0, 0],
            [4, 0, 0],
            [0, 0, 0],
        ]
        zero_matrix(matrix)
        self.assertEqual(expected, matrix)
