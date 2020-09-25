import unittest


def tic_tac_toe_winner(board):
    row_winner = check_rows(board)
    if row_winner:
        return row_winner

    col_winner = check_cols(board)
    if col_winner:
        return col_winner

    diag_winner = check_diags(board)
    if diag_winner:
        return diag_winner


def check_rows(board):
    n = len(board)
    for row in range(n):
        icon = board[row][0]
        if icon != "" and all([board[row][col] == icon for col in range(n)]):
            return icon


def check_cols(board):
    n = len(board)
    for col in range(n):
        icon = board[0][col]
        if icon != "" and all([board[row][col] == icon for row in range(n)]):
            return icon


def check_diags(board):
    n = len(board)
    icon = board[0][0]
    if icon != "" and all([board[col][col] == icon for col in range(n)]):
        return icon

    icon = board[0][n - 1]
    if icon != "" and all([board[col][n - 1 - col] == icon for col in range(n)]):
        return icon


class Test(unittest.TestCase):
    def test_parens(self):
        board = [
            ["X", "O", "X"],
            ["O", "O", "X"],
            ["", "O", ""],
        ]
        self.assertEqual("O", tic_tac_toe_winner(board))

        board = [
            ["X", "X", "X"],
            ["O", "O", "X"],
            ["", "O", ""],
        ]
        self.assertEqual("X", tic_tac_toe_winner(board))

        board = [
            ["X", "O", "O"],
            ["O", "X", "X"],
            ["", "O", "X"],
        ]
        self.assertEqual("X", tic_tac_toe_winner(board))

        board = [
            ["X", "O", "O"],
            ["O", "O", "X"],
            ["O", "X", "X"],
        ]
        self.assertEqual("O", tic_tac_toe_winner(board))

        board = [
            ["X", "O", "O"],
            ["O", "X", "X"],
            ["O", "X", "O"],
        ]
        self.assertEqual(None, tic_tac_toe_winner(board))
