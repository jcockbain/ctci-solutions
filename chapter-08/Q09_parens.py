import unittest


def parens(n):
    if n == 1:
        return ["()"]
    res = set()
    current_parens = parens(n - 1)
    for par in current_parens:
        res.add("(" + par + ")")
        res.add("()" + par)
        res.add(par + "()")
    return list(res)


def parens_2(n):
    return build_parens(n, n)


def build_parens(left, right):
    if left == 0 and right == 0:
        return [""]
    res = []
    if left > 0:
        for s in build_parens(left - 1, right):
            res.append("(" + s)
    if right > left:
        for s in build_parens(left, right - 1):
            res.append(")" + s)
    return res


class Test(unittest.TestCase):
    def test_parens(self):
        self.assertCountEqual(["()"], parens(1))
        self.assertCountEqual(["(())", "()()"], parens(2))

        self.assertCountEqual(
            ["((()))", "(()())", "()(())", "(())()", "()()()"], parens(3),
        )

        self.assertCountEqual(["()"], parens_2(1))
        self.assertCountEqual(["(())", "()()"], parens_2(2))

        self.assertCountEqual(
            ["((()))", "(()())", "()(())", "(())()", "()()()"], parens_2(3),
        )
