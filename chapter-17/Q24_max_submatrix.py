import unittest

# TODO: O(N^3) solution


def max_submatrix(matrix):
    h, w = len(matrix), len(matrix[0])

    max_sum = matrix[0][0]
    precomputed_sums = precompute_sums(matrix)
    for row_1 in range(h):
        for row_2 in range(row_1, h):
            for col_1 in range(w):
                for col_2 in range(col_1, w):
                    sub_sum = get_sum(precomputed_sums, row_1, row_2, col_1, col_2)
                    max_sum = max(sub_sum, max_sum)
    return max_sum


def precompute_sums(matrix):
    h, w = len(matrix), len(matrix[0])
    precomputed_sums = [[0 for _ in range(w)] for _ in range(w)]
    for r in range(h):
        for c in range(w):
            left = 0 if c == 0 else precomputed_sums[r][c - 1]
            top = 0 if r == 0 else precomputed_sums[r - 1][c]
            diag = 0 if r == 0 or c == 0 else precomputed_sums[r - 1][c - 1]
            precomputed_sums[r][c] = left + top - diag + matrix[r][c]
    return precomputed_sums


def get_sum(precomputed_sums, row_1, row_2, col_1, col_2):
    full = precomputed_sums[row_2][col_2]
    left = 0 if col_1 == 0 else precomputed_sums[row_2][col_1 - 1]
    top = 0 if row_1 == 0 else precomputed_sums[row_1 - 1][col_2]
    diag = 0 if col_1 == 0 or row_1 == 0 else precomputed_sums[row_1 - 1][col_1 - 1]
    return full - left - top + diag


class Test(unittest.TestCase):
    def test_max_black_square(self):
        matrix = [[12, 3, -4], [3, -5, 1], [3, 2, 1]]
        self.assertEqual(18, max_submatrix(matrix))

        matrix = [[12, 3], [3, 5]]
        self.assertEqual(23, max_submatrix(matrix))

        matrix = [[-12, -3], [-3, -5]]
        self.assertEqual(-3, max_submatrix(matrix))
