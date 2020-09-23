import unittest


def string_to_bool(s):
    return s == "1"


def boolean_evaluation(s, result):

    if len(s) == 0:
        return 0

    if len(s) == 1:
        return 1 if string_to_bool(s) == result else 0

    ways = 0
    for i in range(1, len(s), 2):
        c = s[i]
        left = s[:i]
        right = s[i + 1 :]

        left_true = boolean_evaluation(left, True)
        left_false = boolean_evaluation(left, False)
        right_true = boolean_evaluation(right, True)
        right_false = boolean_evaluation(right, False)

        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if c == "^":
            total_true = (left_true * right_false) + (right_true * left_false)
        elif c == "&":
            total_true = left_true * right_true
        elif c == "|":
            total_true = (
                (right_true * left_true)
                + (left_true * right_false)
                + (left_false * right_true)
            )

        if result:
            ways += total_true
        else:
            ways += total - total_true

    return ways


class Test(unittest.TestCase):
    def test_boolean_evaluation(self):
        self.assertEqual(2, boolean_evaluation("1^0|0|1", False))
        self.assertEqual(10, boolean_evaluation("0&0&0&1^1|0", True))
        self.assertEqual(0, boolean_evaluation("", True))
