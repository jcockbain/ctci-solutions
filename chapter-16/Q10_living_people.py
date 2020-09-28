import unittest


def living_people(lives):
    births, deaths = [], []
    change = [0] * 102
    for life in lives:
        birth, death = life
        change[birth - 1900] += 1
        change[death - 1900 + 1] -= 1

    alive, max_alive, max_year = 0, 0, None
    for i in range(102):
        alive += change[i]
        if alive > max_alive:
            max_alive = alive
            max_year = i
    return 1900 + max_year


class Test(unittest.TestCase):
    def test_living_people(self):
        lives = [(1905, 1980), (1980, 1999)]
        self.assertEqual(1980, living_people(lives))

        lives = [(1905, 1940), (1935, 1980), (1939, 1939)]
        self.assertEqual(1939, living_people(lives))
