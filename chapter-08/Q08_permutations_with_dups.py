import unittest


def permutations_with_dups(s):
    if len(s) <= 1:
        return s
    res = set()
    permutations = permutations_with_dups(s[1:])
    for perm in permutations:
        for i in range(len(perm) + 1):
            res.add(perm[:i] + s[0] + perm[i:])
    return list(res)


class Test(unittest.TestCase):
    def test_permutation(self):
        s = "off"
        expected = ["ffo", "fof", "off"]
        self.assertEqual(sorted(expected), sorted(permutations_with_dups(s)))
