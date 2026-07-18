#!/usr/bin/python3
"""Defines a MagicClass matching a specific bytecode."""
import math


class MagicClass:
    """Represent a magic class matching bytecode."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Args:
            radius (int or float): The radius of the new MagicClass.
        """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """Return the circumference of the MagicClass."""
        return 2 * math.pi * self._MagicClass__radius
