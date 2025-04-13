import unittest
from app import (
    is_valid_email,
    calculate_rectangle_area,
    filter_even_numbers,
    convert_date_format,
    is_palindrome
)


class TestApp(unittest.TestCase):
    def setUp(self):
        """
        Prepare reusable test data for all tests.
        """
        self.valid_emails = ["a@b.com", "user123@example.co.uk", "john.doe@domain.pl"]
        self.invalid_emails = ["a@b", "plainaddress", "@missingusername.com"]

        self.edge_dimensions = [(0, 10), (10, 0), (0, 0)]  # Edge cases for dimensions
        self.invalid_dimensions = [(-1, 5), (5, -1), (-1, -1)]  # Invalid values

        self.numbers_lists = [
            ([1, 2, 3, 4], [2, 4]),          # Standard case
            ([0, -2, -3, 5], [0, -2]),       # Includes zero and negatives
            ([1.5, "2", 4], [4])             # Filter only integers
        ]

        self.valid_dates = [
            ("2023-01-01", "01.01.2023"),    # Regular date
            ("1999-12-31", "31.12.1999")     # Date before Y2K
        ]
        self.invalid_dates = ["31-12-1999", "not-a-date", "2023-02-30"]  # Invalid formats and impossible date

        self.palindromes = [
            "Kajak",                         # Single word with mixed letters
            "Kobyła ma mały bok",           # Polish sentence with spaces and capital letters
            "No lemon, no melon"            # English palindrome with punctuation and spaces
        ]
        self.not_palindromes = [
            "Python", "Hello world", "Szczecin"  # These are not palindromes
        ]

    # === EMAIL ===
    def test_valid_emails(self):
        """Test valid email formats. Function should return True."""
        for email in self.valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

    def test_invalid_emails(self):
        """Test invalid email formats – missing '@', domain, etc. Should return False."""
        for email in self.invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))

    # === AREA ===
    def test_area_regular_case(self):
        """Standard case: valid dimensions should return correct area."""
        self.assertEqual(calculate_rectangle_area(5, 3), 15)

    def test_area_edge_cases(self):
        """Edge cases where one side is zero – area should be 0."""
        for width, height in self.edge_dimensions:
            with self.subTest(width=width, height=height):
                self.assertEqual(calculate_rectangle_area(width, height), 0)

    def test_area_invalid_values(self):
        """Negative values – function should raise ValueError."""
        for width, height in self.invalid_dimensions:
            with self.subTest(width=width, height=height):
                with self.assertRaises(ValueError):
                    calculate_rectangle_area(width, height)

    # === EVEN NUMBERS ===
    def test_even_number_filtering(self):
        """Test filtering of even numbers from lists."""
        for input_list, expected in self.numbers_lists:
            with self.subTest(input_list=input_list):
                self.assertEqual(filter_even_numbers(input_list), expected)

    def test_even_number_not_equal(self):
        """Negative test – function should not return odd numbers."""
        result = filter_even_numbers([1, 3, 5])
        self.assertNotEqual(result, [1, 3, 5])  # Should be different
        self.assertEqual(result, [])            # Should be an empty list

    # === DATE FORMAT ===
    def test_valid_date_conversion(self):
        """Test correct conversion from YYYY-MM-DD to DD.MM.YYYY format."""
        for original, expected in self.valid_dates:
            with self.subTest(original=original):
                self.assertEqual(convert_date_format(original), expected)

    def test_invalid_date_conversion(self):
        """Test invalid formats and impossible dates – function should raise ValueError."""
        for date_str in self.invalid_dates:
            with self.subTest(date_str=date_str):
                with self.assertRaises(ValueError):
                    convert_date_format(date_str)

    # === PALINDROMES ===
    def test_palindromes(self):
        """Test various palindromes (should ignore case, spaces, diacritical marks)."""
        for word in self.palindromes:
            with self.subTest(word=word):
                self.assertTrue(is_palindrome(word))

    def test_non_palindromes(self):
        """Test texts that are not palindromes."""
        for word in self.not_palindromes:
            with self.subTest(word=word):
                self.assertFalse(is_palindrome(word))


# Run tests only when this file is executed directly
if __name__ == '__main__':
    unittest.main()

