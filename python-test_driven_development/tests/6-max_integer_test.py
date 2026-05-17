#!/usr/bin/python3
"""Unittests for max_integer function."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a single element list."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with all negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers."""
        self.assertEqual(max_integer([-1, 0, 3, -4]), 3)

    def test_max_at_beginning(self):
        """Test with max value at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_middle(self):
        """Test with max value in the middle."""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_duplicate_values(self):
        """Test with duplicate values."""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_duplicate_max(self):
        """Test with duplicate max values."""
        self.assertEqual(max_integer([4, 4, 1, 2]), 4)

    def test_floats(self):
        """Test with float values."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_int_float(self):
        """Test with mixed integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 2, 3.5]), 3.5)

    def test_zero(self):
        """Test with zero in the list."""
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_no_argument(self):
        """Test with no argument passed."""
        self.assertIsNone(max_integer())

    def test_large_numbers(self):
        """Test with large numbers."""
        self.assertEqual(max_integer([999999, 1000000, 999998]), 1000000)


if __name__ == '__main__':
    unittest.main()
