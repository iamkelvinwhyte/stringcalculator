import unittest
from calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(self.calculator.add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3,4"), 10)

    def test_newline_separator(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            self.calculator.add("-1,2,-3")

    def test_ignore_big_numbers(self):
        self.assertEqual(self.calculator.add("2,1001,3"), 5)

    def test_custom_delimiter_of_any_length(self):
        self.assertEqual(self.calculator.add("//[***]\n1***2***3"), 6)

    def test_multiple_delimiters(self):
        self.assertEqual(self.calculator.add("//[*][%]\n1*2%3"), 6)

    def test_multiple_delimiters_of_any_length(self):
        self.assertEqual(self.calculator.add("//[**][%%%]\n1**2%%%3"), 6)


if __name__ == '__main__':
    unittest.main()
