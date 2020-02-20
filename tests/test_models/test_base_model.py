#!/usr/bin/python3
"""
Unit testing Module
"""
from datetime import datetime
import unittest
import inspect
import pep8 as pycodestyle
from unittest import mock
import models
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__

class TestBMDocs(unittest.TestCase): 
    """
    Tests to check all documentation and style of BaseModel class
    """
    @classmethod
    def setUpClass(self):
        """SetUp docstring tests"""
    self.base_functions = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8(self):
        """Test pep8"""
         for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    #def test_ModDocst(self):
        #"""Test module DocString"""
    #def test_classDocst(self):
        #"""Test Class DocString"""

