#!/usr/bin/python3
"""
Unit test for Base Class
"""

import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test for Base class
    """

    def test_docstring(self):
        """
        Test docstring
        """
        self.assertIsNotNone(Base.__doc__)
