import importlib.util
import unittest
from pathlib import Path


spec = importlib.util.spec_from_file_location(
    "calculator", Path(__file__).with_name("main-RDP.py")
)
calculator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(calculator)


class CalculatorTests(unittest.TestCase):
    def test_precedence_and_associativity(self):
        self.assertEqual(calculator.evaluate("2 + 3 * 4"), 14)
        self.assertEqual(calculator.evaluate("10 - 3 - 2"), 5)
        self.assertEqual(calculator.evaluate("20 / 5 / 2"), 2)

    def test_parentheses_and_nesting(self):
        self.assertEqual(calculator.evaluate("(2 + 3) * 4"), 20)
        self.assertEqual(calculator.evaluate("2 * (3 + (4 * 2))"), 22)

    def test_unary_operators_and_decimals(self):
        self.assertEqual(calculator.evaluate("-2 + 3"), 1)
        self.assertEqual(calculator.evaluate(" .5 + 1.25 "), 1.75)

    def test_invalid_expressions(self):
        for expression in ("", "2 +", "2 ** 3", "(2 + 3", "2 + 3)", "2.3.4"):
            with self.subTest(expression=expression):
                with self.assertRaises(calculator.ParseError):
                    calculator.evaluate(expression)

    def test_division_by_zero(self):
        with self.assertRaisesRegex(calculator.ParseError, "Division by zero"):
            calculator.evaluate("10 / 0")


if __name__ == "__main__":
    unittest.main()
