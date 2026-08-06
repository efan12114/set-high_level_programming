#!/usr/bin/python3
"""Unittest module for Base class."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base class functionality."""

    def test_auto_id(self):
        """Test incremental auto ID generation."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_custom_id(self):
        """Test passing custom ID."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test to_json_string with None or empty."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string_none(self):
        """Test from_json_string with None or empty."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_create_rectangle(self):
        """Test create class method for Rectangle."""
        r1 = Rectangle(3, 5, 1, 2, 99)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_save_and_load_file(self):
        """Test save_to_file and load_from_file methods."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        output = Rectangle.load_from_file()
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0].id, r1.id)
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
