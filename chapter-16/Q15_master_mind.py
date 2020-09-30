import unittest
from collections import Counter


def master_mind(guess, solution):
    hits, pseudo_hits = 0, 0
    remaining_guess, remaining_solution = [], []
    for i in range(len(guess)):
        guess_char, solution_char = guess[i], solution[i]
        if guess_char == solution_char:
            hits += 1
        else:
            remaining_guess.append(guess_char)
            remaining_solution.append(solution_char)

    guess_counter, solution_counter = (
        Counter(remaining_guess),
        Counter(remaining_solution),
    )

    for guess in guess_counter:
        if guess in solution_counter:
            pseudo_hits += min(guess_counter[guess], solution_counter[guess])

    return hits, pseudo_hits


class Test(unittest.TestCase):
    def test_master_mind(self):
        self.assertEqual((1, 1), master_mind("GGRR", "RGBY"))
        self.assertEqual((0, 4), master_mind("GRYB", "RGBY"))
        self.assertEqual((4, 0), master_mind("GRBY", "GRBY"))
