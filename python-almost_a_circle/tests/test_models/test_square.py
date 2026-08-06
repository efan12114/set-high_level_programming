#!/usr/bin/python3
"""Unittest module for Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square class functionality."""

    def test_init(self):
        """Test Square initialization."""
        s = Square(5, 1, 2, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 10)

    def test_size_setter(self):
        """Test size property setter updates width and height."""
        s = Square(5)
        s.size = 8
        self.assertEqual(s.width, 8)
        self.assertEqual(s.height, 8)

    def test_str(self):
        """Test Square __str__ representation."""
        s = Square(5, 2, 1, 3)
        self.assertEqual(str(s), "[Square] (3) 2/1 - 5")

    def test_to_dictionary(self):
        """Test to_dictionary output keys."""
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 1, "size": 10, "x": 2, "y": 1})


if __name__ == "__main__":
    unittest.main()
