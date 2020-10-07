import unittest


class SquareCell:
    def __init__(self):
        self.zeros_below = 0
        self.zeros_right = 0


class Square:
    def __init__(self, r, c, side_length):
        self.upper_left = (r, c)
        self.side_length = side_length


def max_black_square(matrix):
    processed_matrix = process_matrix(matrix)
    for i in range(len(matrix), 0, -1):
        square = find_square_with_size(processed_matrix, i)
        if square:
            return square


def find_square_with_size(matrix, size):
    count = len(matrix) - size + 1

    for r in range(count):
        for c in range(count):
            if is_square(matrix, r, c, size):
                return Square(r, c, size)


def is_square(matrix, r, c, size):
    top_left = matrix[r][c]
    top_right = matrix[r][c + size - 1]
    bottom_left = matrix[r + c + size - 1][c]

    if (
        top_left.zeros_right < size
        or top_left.zeros_below < size
        or top_right.zeros_below < size
        or bottom_left.zeros_right < size
    ):
        return False
    return True


def process_matrix(matrix):
    h, w = len(matrix), len(matrix[0])
    processed = [[SquareCell() for _ in range(w)] for _ in range(h)]
    for r in range(h - 1, -1, -1):
        for c in range(w - 1, -1, -1):
            zeros_right, zeros_below = 0, 0
            if matrix[r][c] == 0:
                zeros_right += 1
                zeros_below += 1
                if c + 1 < w:
                    previous = processed[r][c + 1]
                    zeros_right += previous.zeros_right
                if r + 1 < h:
                    previous = processed[r + 1][c]
                    zeros_below += previous.zeros_below
            processed[r][c].zeros_below = zeros_below
            processed[r][c].zeros_right = zeros_right
    return processed


class Test(unittest.TestCase):
    def test_max_black_square(self):
        matrix = [[1, 0, 1], [0, 0, 1], [0, 0, 1]]
        res = max_black_square(matrix)
        self.assertEqual((1, 0), res.upper_left)
        self.assertEqual(2, res.side_length)
