import simple_calc
import unittest
import sys


class TestAddition(unittest.TestCase):
    """ Test cases for addition function add() """

    def test_addition_integers(self):
        """ Test addition of two integers returns the correct total. """
        result = simple_calc.add(1, 2)
        self.assertEqual(result, 3)
    
    def test_addition_floats(self):
        """ Test addition of two floats returns the correct total. """
        result = simple_calc.add(10.5, 2)
        self.assertEqual(result, 12.5)
    
    @unittest.skip('Skip this test')
    def test_add_strings(self):
        """ Test addition of two strings returns a concantenated string. """
        result = simple_calc.add('abc', 'def')
        self.assertEqual(result, 'abcdef')

    @unittest.skipUnless(sys.platform.startswith("linux"), "requires Linux")
    def test_adding_on_window(self):
        result = simple_calc.add(1, 2)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()


