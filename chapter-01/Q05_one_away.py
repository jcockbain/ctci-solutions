import unittest


def one_away(a, b):
    if len(a) == len(b):
        return one_replace_away(a, b)
    elif len(a) == len(b) + 1:
        return one_insert_away(b, a)
    elif len(b) == len(a) + 1:
        return one_insert_away(a, b)
    else:
        return False


def one_replace_away(s1, s2):
    found_difference = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_difference:
                return False
            found_difference = True
    return True


def one_insert_away(short, long):
    i1, i2 = 0, 0
    while i1 < len(short) and i2 < len(long):
        if short[i1] != long[i2]:
            if i1 != i2:
                return False
            i2 += 1
        else:
            i1 += 1
            i2 += 1
    return True


class Test(unittest.TestCase):
    def test_one_away(self):
        self.assertEqual(True, one_away("pale", "ple"))
        self.assertEqual(True, one_away("ple", "pale"))
        self.assertEqual(True, one_away("pales", "pale"))
        self.assertEqual(True, one_away("pale", "bale"))
        self.assertEqual(False, one_away("plae", "bae"))
        self.assertEqual(False, one_away("plae", "ploy"))
        self.assertEqual(False, one_away("plae", "plaeyy"))
