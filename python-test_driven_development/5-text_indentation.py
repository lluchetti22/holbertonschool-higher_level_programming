#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char in ".?:":
            print(char)
            print()
        else:
            print(char, end="")
