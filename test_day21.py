
import unittest

from day21 import numbers_until_zero, odd_numbers


class TestBreakAndContinue(unittest.TestCase):

    def test_break_at_zero(self):
        self.assertEqual(
            numbers_until_zero([2, 4, 0, 6, 8]),
            [2, 4, 0]
        )

    def test_break_when_zero_is_first(self):
        self.assertEqual(
            numbers_until_zero([0, 1, 2]),
            [0]
        )

    def test_continue_skips_even_numbers(self):
        self.assertEqual(
            odd_numbers([1, 2, 3, 4, 5]),
            [1, 3, 5]
        )

    def test_continue_with_all_even_numbers(self):
        self.assertEqual(
            odd_numbers([2, 4, 6]),
            []
        )

    def test_empty_list(self):
        self.assertEqual(odd_numbers([]), [])


if __name__ == "__main__":
    unittest.main()
