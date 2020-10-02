import unittest


def split_by_operators(exp):
    operators = ["/", "*", "+", "-"]
    split_arr = []
    current_number = ""
    for c in exp:
        if c in operators:
            if current_number:
                split_arr.append(int(current_number))
                current_number = ""
            split_arr.append(c)
        else:
            current_number += c
    if current_number:
        split_arr.append(int(current_number))
    return split_arr


def operate(op):
    if op == "+":
        return lambda a, b: a + b
    if op == "-":
        return lambda a, b: a - b
    if op == "*":
        return lambda a, b: a * b
    if op == "/":
        return lambda a, b: a / b


def calculator(exp):
    operators = ["/", "*", "+", "-"]
    split_arr = split_by_operators(exp)
    while len(split_arr) > 1:
        for operator in operators:
            while operator in split_arr:
                idx = split_arr.index(operator)
                val = operate(operator)(split_arr[idx - 1], split_arr[idx + 1])
                split_arr = split_arr[: idx - 1] + [val] + split_arr[idx + 2 :]
    return split_arr[0]


class Test(unittest.TestCase):
    def test_split_by_operators(self):
        exp = "2*3+5/6*3+15"
        self.assertEqual(
            [2, "*", 3, "+", 5, "/", 6, "*", 3, "+", 15], split_by_operators(exp)
        )

    def test_calculator(self):
        exp = "2*3+5/6*3+15"
        self.assertEqual(23.5, calculator(exp))
        exp = "3-15"
        self.assertEqual(-12, calculator(exp))
