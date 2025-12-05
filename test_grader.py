import unittest
from grader import *

class TestDataProcessor(unittest.TestCase):
    def test_analyze_text_normal_string(self):
        expected = {'length': 11, 'word_count': 2, 'char_count': {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}, 'is_palindrome': False}
        self.assertEqual(analyze_text("hello world"), expected)

    def test_analyze_text_empty_string(self):
        expected = {'length': 0, 'word_count': 0, 'char_count': {}, 'is_palindrome': False}
        self.assertEqual(analyze_text(""), expected)

    def test_analyze_text_whitespace_string(self):
        expected = {'length': 5, 'word_count': 0, 'char_count': {' ': 3, '\t': 1, '\n': 1}, 'is_palindrome': False}
        self.assertEqual(analyze_text("   \t\n"), expected)

    def test_analyze_text_simple_palindrome(self):
        expected = {'length': 7, 'word_count': 1, 'char_count': {'r': 2, 'a': 2, 'c': 2, 'e': 1}, 'is_palindrome': True}
        self.assertEqual(analyze_text("racecar"), expected)

    def test_analyze_text_complex_palindrome(self):
        text = "A man, a plan, a canal: Panama"
        expected = {'length': 30, 'word_count': 7, 'char_count': {'A': 1, ' ': 6, 'm': 2, 'a': 9, 'n': 4, ',': 2, 'p': 1, 'l': 2, 'c': 1, ':': 1, 'P': 1}, 'is_palindrome': True}
        self.assertEqual(analyze_text(text), expected)

    def test_analyze_text_non_palindrome(self):
        expected = {'length': 5, 'word_count': 1, 'char_count': {'h': 1, 'e': 1, 'l': 2, 'o': 1}, 'is_palindrome': False}
        self.assertEqual(analyze_text("hello"), expected)

    def test_analyze_text_case_sensitive_palindrome(self):
        expected = {'length': 4, 'word_count': 1, 'char_count': {'N': 1, 'o': 2, 'n': 1}, 'is_palindrome': True}
        self.assertEqual(analyze_text("Noon"), expected)

    def test_analyze_text_with_numbers(self):
        expected = {'length': 12, 'word_count': 3, 'char_count': {'1': 2, '2': 2, '3': 2, ' ': 2, 't': 2, 'e': 1, 's': 1}, 'is_palindrome': False}
        self.assertEqual(analyze_text("123 test 123"), expected)

    def test_analyze_text_with_special_chars(self):
        expected = {'length': 5, 'word_count': 1, 'char_count': {'@': 1, '#': 1, '$': 1, '!': 1, '%': 1}, 'is_palindrome': False}
        self.assertEqual(analyze_text("@#$!%"), expected)

    def test_analyze_text_single_word(self):
        expected = {'length': 7, 'word_count': 1, 'char_count': {'t': 2, 'e': 1, 's': 1, 'i': 1, 'n': 1, 'g': 1}, 'is_palindrome': False}
        self.assertEqual(analyze_text("testing"), expected)

    def test_analyze_text_non_string_input_int(self):
        with self.assertRaises(TypeError):
            analyze_text(12345)

    def test_analyze_text_non_string_input_list(self):
        with self.assertRaises(TypeError):
            analyze_text(["not", "a", "string"])

    def test_calculate_grade_A(self):
        self.assertEqual(calculate_grade([90, 95, 100]), {'average_score': 95.0, 'letter_grade': 'A'})

    def test_calculate_grade_B(self):
        self.assertEqual(calculate_grade([80, 85, 89]), {'average_score': 84.67, 'letter_grade': 'B'})

    def test_calculate_grade_C(self):
        self.assertEqual(calculate_grade([70, 75, 79]), {'average_score': 74.67, 'letter_grade': 'C'})

    def test_calculate_grade_D(self):
        self.assertEqual(calculate_grade([60, 65, 69]), {'average_score': 64.67, 'letter_grade': 'D'})

    def test_calculate_grade_F(self):
        self.assertEqual(calculate_grade([0, 20, 59]), {'average_score': 26.33, 'letter_grade': 'F'})

    def test_calculate_grade_boundary_A(self):
        self.assertEqual(calculate_grade([90, 90, 90]), {'average_score': 90.0, 'letter_grade': 'A'})
        self.assertEqual(calculate_grade([89, 90, 91]), {'average_score': 90.0, 'letter_grade': 'A'})

    def test_calculate_grade_boundary_B(self):
        self.assertEqual(calculate_grade([80]), {'average_score': 80.0, 'letter_grade': 'B'})
        self.assertEqual(calculate_grade([79.9]), {'average_score': 79.9, 'letter_grade': 'C'})

    def test_calculate_grade_boundary_C(self):
        self.assertEqual(calculate_grade([70, 70]), {'average_score': 70.0, 'letter_grade': 'C'})
        self.assertEqual(calculate_grade([69.9, 70.1]), {'average_score': 70.0, 'letter_grade': 'C'})

    def test_calculate_grade_boundary_D(self):
        self.assertEqual(calculate_grade([60]), {'average_score': 60.0, 'letter_grade': 'D'})
        self.assertEqual(calculate_grade([59.9, 60.1]), {'average_score': 60.0, 'letter_grade': 'D'})

    def test_calculate_grade_with_floats(self):
        self.assertEqual(calculate_grade([85.5, 92.3, 88.1]), {'average_score': 88.63, 'letter_grade': 'B'})

    def test_calculate_grade_all_zeros(self):
        self.assertEqual(calculate_grade([0, 0, 0]), {'average_score': 0.0, 'letter_grade': 'F'})

    def test_calculate_grade_all_hundreds(self):
        self.assertEqual(calculate_grade([100, 100]), {'average_score': 100.0, 'letter_grade': 'A'})

    def test_calculate_grade_single_score(self):
        self.assertEqual(calculate_grade([75]), {'average_score': 75.0, 'letter_grade': 'C'})

    def test_calculate_grade_invalid_score_negative(self):
        with self.assertRaises(ValueError):
            calculate_grade([90, -5, 80])

    def test_calculate_grade_invalid_score_above_100(self):
        with self.assertRaises(ValueError):
            calculate_grade([90, 101, 80])

    def test_calculate_grade_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_grade([])

    def test_calculate_grade_non_list_input(self):
        with self.assertRaises(TypeError):
            calculate_grade("not a list")

    def test_calculate_grade_list_with_non_numeric(self):
        with self.assertRaises(TypeError):
            calculate_grade([90, "85", 100])

if __name__ == '__main__':
    unittest.main()
    