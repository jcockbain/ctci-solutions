import unittest


def pattern_matching(pattern, value):
    if len(value) == 0:
        return True
    if len(pattern) == 0:
        return False

    len_value = len(value)
    pattern = normalize_pattern(pattern)
    count_a = pattern.count("a")
    count_b = pattern.count("b")

    for i in range(len_value + 1):
        substring_1 = value[:i]
        len_all_b = len_value - (count_a * i)

        if count_b and len_all_b % count_b == 0:
            len_b = int(len_all_b / count_b)
            first_b_idx = i * pattern.index("b")
            substring_2 = value[first_b_idx : first_b_idx + len_b]
            if build_pattern(substring_1, substring_2, pattern) == value:
                return True
        elif not count_b:
            if build_pattern(substring_1, "", pattern) == value:
                return True
    return False


def get_string(a, b, char):
    return a if char == "a" else b


def build_pattern(a, b, pattern):
    return "".join([get_string(a, b, char) for char in pattern])


def flip(c):
    return "a" if c == "b" else "b"


def normalize_pattern(pattern):
    if pattern[0] == "a":
        return pattern
    return "".join([flip(c) for c in pattern])


class Test(unittest.TestCase):
    def test_normalize_pattern(self):
        self.assertEqual("aba", normalize_pattern("bab"))
        self.assertEqual("abab", normalize_pattern("baba"))

    def test_pattern_matching(self):
        s = "catcatgocatgo"
        self.assertEqual(True, pattern_matching("aabab", s))
        self.assertEqual(True, pattern_matching("ab", s))
        self.assertEqual(True, pattern_matching("ba", s))
        self.assertEqual(False, pattern_matching("abab", s))
        self.assertEqual(True, pattern_matching("a", s))
        self.assertEqual(False, pattern_matching("aaa", s))

        self.assertEqual(True, pattern_matching("a", ""))
        self.assertEqual(False, pattern_matching("", "cat"))
