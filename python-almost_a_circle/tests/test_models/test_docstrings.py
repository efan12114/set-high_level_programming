#!/usr/bin/python3
"""Unittest module for checking docstrings across all modules."""
import inspect
import unittest
import models.base
import models.rectangle
import models.square
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestDocstrings(unittest.TestCase):
    """Tests for module, class, and method docstrings."""

    def test_module_docstrings(self):
        """Test that modules have docstrings."""
        self.assertTrue(len(models.base.__doc__) > 1)
        self.assertTrue(len(models.rectangle.__doc__) > 1)
        self.assertTrue(len(models.square.__doc__) > 1)

    def test_class_docstrings(self):
        """Test that classes have docstrings."""
        self.assertTrue(len(Base.__doc__) > 1)
        self.assertTrue(len(Rectangle.__doc__) > 1)
        self.assertTrue(len(Square.__doc__) > 1)

    def test_method_docstrings(self):
        """Test that all methods in classes have docstrings."""
        for cls in [Base, Rectangle, Square]:
            for name, func in inspect.getmembers(cls, inspect.isfunction):
                self.assertTrue(
                    len(func.__doc__) > 1,
                    f"Missing docstring in {cls.__name__}.{name}"
                )


if __name__ == "__main__":
    unittest.main()
