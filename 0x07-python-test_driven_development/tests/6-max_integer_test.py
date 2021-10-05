#!/usr/bin/python3
""" testing module """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class to test maxinteger function"""
    def test_find_max(self):
        """give the max of the list"""
        empty = [10, 8, 15, 20]
        result = max_integer(empty)
        self.assertEqual(result, 20)
    def test_empty_list(self):
        """give the max of the list"""
        empty = []
        result = max_integer(empty)
        self.assertEqual(result, None)
    def test_string(self):
        """Test a string."""
        string = "chamchoun"
        result = max_integer(string)
        self.assertEqual(result, 'u')
    def test_string(self):
        """Test a string."""
        strings = ["chamchoun", "is", "awesome"]
        result = max_integer(strings)
        self.assertEqual(result, 'is')

if __name__ == '__main__':
    main()
