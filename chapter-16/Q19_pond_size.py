import unittest


def pond_size(matrix):
    h, w = len(matrix), len(matrix[0])
    visited = set()
    pond_sizes = []

    def dfs(start):
        stack = [start]
        visited.add(start)
        pond_size = 0
        while stack:
            node = stack.pop()
            pond_size += 1
            neighbours = get_neighbours(node)
            for (r, c) in neighbours:
                if (
                    0 <= r < h
                    and 0 <= c < w
                    and matrix[r][c] == 0
                    and (r, c) not in visited
                ):
                    stack.append((r, c))
                    visited.add((r, c))
        return pond_size

    for r in range(h):
        for c in range(w):
            if matrix[r][c] == 0 and (r, c) not in visited:
                pond_size = dfs((r, c))
                pond_sizes.append(pond_size)

    return pond_sizes


def get_neighbours(point):
    res = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if not (dr == 0 and dc == 0):
                res.append((point[0] + dr, point[1] + dc))
    return res


class Test(unittest.TestCase):
    def test_get_neighbours(self):
        self.assertEqual(
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)],
            get_neighbours((1, 1)),
        )

    def test_pond_size(self):
        matrix = [[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]
        self.assertEqual([2, 4, 1], pond_size(matrix))
