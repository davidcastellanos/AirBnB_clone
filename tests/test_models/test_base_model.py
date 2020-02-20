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

    def test_ModDocst(self):
        """Test module DocString"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs the docStr")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs the docStr")

    def test_classDocst(self):
        """Test Class DocString"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs docStr")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs docStr")
     
     def test_FuncDocStr(self):
        """Test for presence of docstr in BaseModel methods"""
        for functions in self.BaseModel:
            with self.subTest(function=functions):
                self.assertIsNot(
                    functions[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(functions[0])
                )
                self.assertTrue(
                    len(functions[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(functions[0])
                )
