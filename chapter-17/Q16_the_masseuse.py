import unittest


def maximum_mins(requests, idx=0):
    one_away = requests[0]
    two_away = 0
    for i in range(len(requests)):
        current_one_way = one_away
        one_away = max(two_away + requests[i], one_away)
        two_away = current_one_way
    return one_away


class Test(unittest.TestCase):
    def test_maximum_mins(self):
        self.assertEqual(180, maximum_mins([30, 15, 60, 75, 45, 15, 15, 45]))
