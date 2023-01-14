from calculate import Calculate
import unittest


class Calc_test(unittest.TestCase):
    def test_no_numbers_test(self):
        calc = Calculate()
        self.assertFalse(calc.can_calculate("hello world"))

    def test_right_numbers_and_wrong_sign(self):
        calc = Calculate()
        self.assertFalse(calc.can_calculate("3 puls 4"))

    def test_right_numbers_and_two_wrong_signs(self):
        calc = Calculate()
        self.assertFalse(calc.can_calculate("3 by divide 4"))

    def test_zero_division(self):
        calc = Calculate()
        self.assertTrue(calc.can_calculate("3 divide 0"))

    def test_plus_sign(self):
        calc = Calculate()
        self.assertTrue(calc.can_calculate("3 + 4"))

    def test_plus_word(self):
        calc = Calculate()
        self.assertTrue(calc.can_calculate("3 plus 4"))

    def test_minus_sign(self):
        calc = Calculate()
        self.assertTrue(calc.can_calculate("3 - 4"))

    def test_minus_word(self):
        calc = Calculate()
        self.assertTrue(calc.can_calculate("3 minus 4"))

    def test_by_sign(self):
        calc = Calculate()
        self.assertTrue(calc.can_calculate("3 * 4"))

    def test_by_word(self):
        calc = Calculate()
        self.assertTrue(calc.can_calculate("3 by 4"))

    def test_divide_sign(self):
        calc = Calculate()
        self.assertTrue(calc.can_calculate("3 / 4"))

    def test_divide_word(self):
        calc = Calculate()
        self.assertTrue(calc.can_calculate("3 divide 4"))

    def test_divide_by_word(self):
        calc = Calculate()
        self.assertTrue(calc.can_calculate("3 divide by 4"))

    def test_divided_by_word(self):
        calc = Calculate()
        self.assertTrue(calc.can_calculate("3 divided by 4"))

    def test_square_root_word(self):
        calc = Calculate()
        self.assertTrue(calc.can_calculate("3 by square root 4"))

    def test_square_root(self):
        calc = Calculate()
        calc.can_calculate("3 by square root 4")
        self.assertEqual(calc.get_result(), "The answer is 6")


if __name__ == "__main__":
    unittest.main()
