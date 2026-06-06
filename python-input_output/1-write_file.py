#!/usr/bin/python3
"""Module for writing a string to a text file and returning char count."""


def write_file(filename="", text=""):
    """Read a text file (UTF-8) and print its content to stdout."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
