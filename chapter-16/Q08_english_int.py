import unittest

SINGLE_DIGIT = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}
TEENS = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}
TENS = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}
LARGE_NUMBERS = ["", "thousand", "million", "billion"]


def english_int(n):
    if n == 0:
        return "zero"
    shifts, res, add_and = 0, [], False
    while n > 0:
        rem = n % 1000
        if shifts == 0 and rem < 100:
            add_and = True
        if rem != 0:
            current_chunk = english_int_below_one_thousand(rem)
            current_chunk += " {}".format(LARGE_NUMBERS[shifts])
            if add_and and len(res) == 1:
                current_chunk += " {} ".format("and")
                add_and = False
            elif shifts > 0 and len(res) > 0:
                current_chunk += ","
            current_chunk = current_chunk.strip()
            res.append(current_chunk)
        n = n // 1000
        shifts += 1
    return " ".join(reversed(res))


def english_int_below_one_thousand(n):
    if n < 10:
        return SINGLE_DIGIT[n]
    if n < 20:
        return TEENS[n]
    if n < 100:
        tens = n // 10
        digits = n % 10
        res = TENS[10 * tens]
        if digits != 0:
            res += " {}".format(SINGLE_DIGIT[digits])
        return res
    else:
        hundreds = n // 100
        rem = n % 100
        res = "{} hundred".format(SINGLE_DIGIT[hundreds])
        if rem != 0:
            res += " and {}".format(english_int_below_one_thousand(rem))
        return res


class Test(unittest.TestCase):
    def test_english_int(self):
        self.assertEqual("zero", english_int(0))
        self.assertEqual("one", english_int(1))
        self.assertEqual("nineteen", english_int(19))
        self.assertEqual("twenty", english_int(20))
        self.assertEqual("twenty one", english_int(21))
        self.assertEqual("one hundred", english_int(100))
        self.assertEqual("three hundred and forty seven", english_int(347))
        self.assertEqual("one hundred thousand", english_int(100000))
        self.assertEqual("one million", english_int(1000000))
        self.assertEqual(
            "one million, one hundred thousand, one hundred and forty two",
            english_int(1100142),
        )
        self.assertEqual(
            "one hundred and forty seven thousand, three hundred and twelve",
            english_int(147312),
        )
        self.assertEqual("one thousand and two", english_int(1002))
        self.assertEqual("two thousand and twelve", english_int(2012))
        self.assertEqual("eight thousand, one hundred", english_int(8100))
        self.assertEqual(
            "seventy three billion, nine hundred and ninety eight million and eighty",
            english_int(73998000080),
        )
