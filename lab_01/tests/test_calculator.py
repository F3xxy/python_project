import unittest

from toolkit.calculator import calculate
from toolkit.errors import CalcError


class TestCalculatorResults(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(calculate("1 + 2"), 3.0)
        self.assertEqual(calculate("5 - 8"), -3.0)
        self.assertEqual(calculate("4 * 2.5"), 10.0)
        self.assertEqual(calculate("7 / 2"), 3.5)

    def test_extra_operations(self):
        self.assertEqual(calculate("7 // 2"), 3.0)
        self.assertEqual(calculate("7 % 3"), 1.0)

    def test_priority(self):
        self.assertEqual(calculate("2 + 3 * 4"), 14.0)
        self.assertEqual(calculate("10 - 4 / 2"), 8.0)

    def test_left_associativity(self):
        self.assertEqual(calculate("8 - 3 - 2"), 3.0)
        self.assertEqual(calculate("16 / 4 / 2"), 2.0)

    def test_parentheses(self):
        self.assertEqual(calculate("(1 + 2) * 3"), 9.0)
        self.assertEqual(calculate("2 * (3 + 4) - 5"), 9.0)
        self.assertEqual(calculate("((2))"), 2.0)

    def test_unary(self):
        self.assertEqual(calculate("-5"), -5.0)
        self.assertEqual(calculate("+5"), 5.0)
        self.assertEqual(calculate("2 * -3"), -6.0)
        self.assertEqual(calculate("2 - -3"), 5.0)
        self.assertEqual(calculate("-(2 + 3)"), -5.0)
        self.assertEqual(calculate("--5"), 5.0)

    def test_spaces_ignored(self):
        self.assertEqual(calculate("  3.5*2  "), 7.0)
        self.assertEqual(calculate("3.5*2"), 7.0)

    def test_result_is_float(self):
        self.assertIsInstance(calculate("2 + 2"), float)


class TestCalculatorErrors(unittest.TestCase):
    def assert_error(self, expression):
        with self.assertRaises(CalcError):
            calculate(expression)

    def test_empty(self):
        self.assert_error("")
        self.assert_error("   ")

    def test_invalid_symbol(self):
        self.assert_error("2 $ 3")
        self.assert_error("2 & 3")
        self.assert_error("abc")

    def test_missing_operand(self):
        self.assert_error("2 +")
        self.assert_error("* 3")
        self.assert_error("(2 +)")

    def test_two_operators_in_row(self):
        self.assert_error("2 * / 3")
        self.assert_error("2 // // 3")
        self.assert_error("2 + * 3")

    def test_division_by_zero(self):
        self.assert_error("1 / 0")
        self.assert_error("1 // 0")
        self.assert_error("1 % 0")

    def test_invalid_number(self):
        self.assert_error("1.2.3")
        self.assert_error(".")

    def test_missing_operator(self):
        self.assert_error("2 3")
        self.assert_error("2(3)")
        self.assert_error("(2)(3)")

    def test_brackets(self):
        self.assert_error("(1 + 2")
        self.assert_error("1 + 2)")
        self.assert_error("()")


if __name__ == "__main__":
    unittest.main()