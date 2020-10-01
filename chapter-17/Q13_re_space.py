import unittest


class Result:
    def __init__(self, parsed=" ", invalid=float("inf")):
        self.parsed = parsed
        self.invalid = invalid


def re_space(words, s):
    dp = [None] * len(s)

    def split_words(start):

        if start >= len(s):
            return Result("", 0)

        if not dp[start]:
            best_invalid = float("inf")
            best_parsing = None
            idx = start
            word = ""

            while idx < len(s):
                word += s[idx]
                invalid = len(word) if word not in words else 0
                if invalid <= best_invalid:
                    result = split_words(idx + 1)
                    if invalid + result.invalid <= best_invalid:
                        best_invalid = invalid + result.invalid
                        if result.parsed != "":
                            best_parsing = word + " " + result.parsed
                        else:
                            best_parsing = word
                        if best_invalid == 0:
                            break
                idx += 1
            dp[start] = Result(best_parsing, best_invalid)
        return dp[start]

    return split_words(0)


class Test(unittest.TestCase):
    def test_re_space(self):
        words = set(["looked", "just", "like", "her", "brother"])
        sentence = "jesslookedjustliketimherbrother"
        result = re_space(words, sentence)
        self.assertEqual(7, result.invalid)
        self.assertEqual("jess looked just like tim her brother", result.parsed)
