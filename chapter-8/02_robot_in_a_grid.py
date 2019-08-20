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

    is_at_origin = (row == 0) and (col == 0)

    # if there's a path from the start to here, add my location
    if is_at_origin or is_path(maze, row, col-1, path) or is_path(maze, row-1, col, path):
        point = (row, col)
        path.append(point)
        return True
    return False

# Solution with memoization


def get_path_memoized(maze):
    if maze is None or len(maze) == 0:
        return None
    path = []
    failedPoints = []
    if is_path_memoized(maze, len(maze)-1, len(maze[0])-1, path, failedPoints):
        return path
    return None


def is_path_memoized(maze, row, col, path, failedPoints):
    # If out of bounds or not availabe, return
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    point = (row, col)

    # if we've already visited this cell, return
    if point in failedPoints:
        return False

    is_at_origin = (row == 0) and (col == 0)

    # If there's a path from start to my current location, add my location
    if is_at_origin or is_path_memoized(maze, row, col-1, path, failedPoints) or is_path_memoized(maze, row-1, col, path, failedPoints):
        path.append(point)
        return True

    failedPoints.append(point)
    return False


class Test(unittest.TestCase):
    def test_path_through_grid(self):
        grid = [[True, True], [True, True]]
        grid2 = [[False, False], [False, True]]
        self.assertEqual(get_path_memoized(grid), [(0, 0), (1, 0), (1, 1)])
        self.assertEqual(get_path_memoized(grid2), None)


if __name__ == "__main__":
    unittest.main()
