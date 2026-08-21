#!/usr/bin/python3
"""
Defines an integer addition function.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: first integer or float
        b: second integer or float (default is 98)

    Returns:
        The addition of a and b as an integer.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
