#!/usr/bin/python3
"""Module for adding two integers."""


def add_integer(a, b=98):
    """Adds two integers or floats, casting floats to integers first."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)