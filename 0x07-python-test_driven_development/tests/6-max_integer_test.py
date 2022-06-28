#!/usr/bin/python3
"""Unittest for the max_integer Module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class testing_max_integer(unittest.TestCase):
    """Class test for the max_integer function"""

    def test_middle(self):
        """test with max int at middle
        """
        self.assertAlmostEquals(max_integer([1, 2, 5, 4]), 5)

    def test_end(self):
        """test with max int at end
        """
        self.assertAlmostEquals(max_integer([1, 2, 4, 5]), 5)

    def test_beginning(self):
        """test random numbers
        """
        self.assertAlmostEquals(max_integer([5, 2, 4, 2]), 5)

    def test_only_negative_numbers(self):
        """test with list of all negative numbers
        """
        self.assertAlmostEquals(max_integer([-1, -3, -100, -4]), -1)

    def test_floats(self):
        """test with a list of float values
        """
        self.assertAlmostEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_one_negative_number(self):
        """test with just one negative int
        """
        self.assertAlmostEquals(max_integer([-100]), -100)

    def test_one_number(self):
        """test with one positive int
        """
        self.assertAlmostEquals(max_integer([100]), 100)

    def test_empty(self):
        """test empty list
        """
        self.assertAlmostEqual(max_integer([]), None)

    def test_not_list(self):
        """test with mixed list
        """
        wi = [1, 2, "mao", 4]
        self.assertRaises(TypeError)

        wi = [1, 2, [1, 2, 3], 4]
        self.assertRaises(TypeError)

        wi = [1, 2, (1, 2, 3), 4]
        self.assertRaises(TypeError)

        wi = (2, 2)
        self.assertRaises(TypeError)

        wi = "hello"
        self.assertRaises(TypeError)

    def test_none_and_zero(self):

        wi = []
        self.assertAlmostEqual(max_integer(wi), None)

        wi = [0, 0, 0, 0]
        self.assertAlmostEqual(max_integer(wi), 0)

        self.assertAlmostEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
