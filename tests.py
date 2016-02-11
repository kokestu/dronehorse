#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tests

Tests for dronehorse.

"""

import unittest
import doctest

from dronehorse import classes, planner

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(classes))
    tests.addTests(doctest.DocTestSuite(planner))
    return tests

if __name__ == '__main__':
    unittest.main()
