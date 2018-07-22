import unittest

from test_simple_calc import TestAddition


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestAddition))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()

