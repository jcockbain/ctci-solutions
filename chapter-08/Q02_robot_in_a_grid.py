import unittest
from collections import deque


def recreate_path(start, end, previous_position):
    pos = start
    path = []
    while pos != end:
        if pos not in previous_position:
            return []
        path.append(pos)
        pos = previous_position[pos]
    return path + [end]


def get_path(grid):
    h, w = len(grid), len(grid[0])
    previous_position = {}
    queue = deque([(h - 1, w - 1)])
    directions = [(-1, 0), (0, -1)]

    while queue:
        pos = queue.popleft()
        for xr, xc in directions:
            new_r, new_c = pos[0] + xr, pos[1] + xc
            if (
                0 <= new_r < h
                and 0 <= new_c < w
                and grid[new_r][new_c] == 0
                and (new_r, new_c) not in previous_position
            ):
                previous_position[(new_r, new_c)] = pos
                queue.append((new_r, new_c))

    return recreate_path((0, 0), (h - 1, w - 1), previous_position)


class Test(unittest.TestCase):
    def test_path_through_grid(self):
        grid = [
            [0, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 1, 0],
        ]

        self.assertEqual(
            get_path(grid),
            [
                (0, 0),
                (0, 1),
                (0, 2),
                (0, 3),
                (1, 3),
                (2, 3),
                (2, 4),
                (2, 5),
                (2, 6),
                (3, 6),
            ],
        )


if __name__ == "__main__":
    unittest.main()
