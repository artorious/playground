""" Test docstring tests file: simple_calc_with_docs.py """
import doctest
import simple_calc_with_docs
import unittest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(simple_calc_with_docs))
    return tests

