#!/usr/bin/python3
"""Unittest module for Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class functionality."""

    def test_init(self):
        """Test successful initialization."""
        r = Rectangle(10, 2, 1, 1, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 5)

    def test_type_errors(self):
        """Test validation raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "1")
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, "1")

    def test_value_errors(self):
        """Test validation raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -1)

    def test_area(self):
        """Test area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test __str__ representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


if __name__ == "__main__":
    unittest.main()
