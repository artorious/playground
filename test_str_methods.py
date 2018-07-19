""" A short script to test string methods """
import unittest


class TestStringMethods(unittest.TestCase):
    """ Tests for string methods """
    def test_upper(self):
        """ test str.upper() """
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """ Test str.isupper() """
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """ Test str.split() 
            Handle invalid separator input
        """
        str_sample = 'hello world'
        self.assertEqual(
            str_sample.split(), ['hello', 'world']
        )

        with self.assertRaises(TypeError):
            str_sample.split(2)

if __name__ == '__main__':
    unittest.main()

