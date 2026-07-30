#!/usr/bin/python3
"""Module for reading a text file and printing it to stdout."""

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
