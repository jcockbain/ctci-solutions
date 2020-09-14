import unittest


def sorted_merge(a, b):
    bix = len(b) - 1
    aix = len(a) - len(b) - 1
    while aix >= 0 and bix >= 0:
        if a[aix] > b[bix]:
            a[aix + bix + 1] = a[aix]
            aix -= 1
        else:
            a[aix + bix + 1] = b[bix]
            bix -= 1
    while bix >= 0:
        a[bix] = b[bix]
        bix -= 1


class Test(unittest.TestCase):
    def test_sorted_merge(self):
        a = [1, 2, None, None]
        b = [3, 4]
        sorted_merge(a, b)
        self.assertEqual(a, [1, 2, 3, 4])
