import unittest


def get_path(maze):
    if maze is None or len(maze) == 0:
        return None
    path = []
    if is_path(maze, len(maze) - 1, len(maze[0])-1, path):
        return path
    return None


def is_path(maze, row, col, path):
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    isAtOrigin = (row == 0) and (col == 0)

    # if there's a path from the start to here, add my location
    if isAtOrigin or is_path(maze, row, col-1, path) or is_path(maze, row-1, col, path):
        point = (row, col)
        path.append(point)
        return True
    return False


class Test(unittest.TestCase):
    def test_path_through_grid(self):
        grid = [[True, True], [True, True]]
        grid2 = [[False, False], [False, True]]
        self.assertEqual(get_path(grid), [(0, 0), (1, 0), (1, 1)])
        self.assertEqual(get_path(grid2), None)


if __name__ == "__main__":
    unittest.main()
