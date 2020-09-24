import unittest


def permutations_without_dups(s):
    if len(s) <= 1:
        return s
    res = []
    permutations = permutations_without_dups(s[1:])
    for perm in permutations:
        for i in range(len(perm) + 1):
            res.append(perm[:i] + s[0] + perm[i:])
    return res


class Test(unittest.TestCase):
    def test_permutation(self):
        s = "for"
        expected = ["for", "fro", "orf", "ofr", "rof", "rfo"]
        self.assertCountEqual(expected, permutations_without_dups(s))
