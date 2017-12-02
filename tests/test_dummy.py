#!/bin/env python

import unittest


class TestPass(unittest.TestCase):

    def setUp(self):
        pass

    def test_one(self):
        self.assertTrue(1 == 1)

    def test_two(self):
        self.assertTrue(2 == 2)

    def test_three(self):
        self.assertTrue(3 == 3)

    def tearDown(self):
        pass
