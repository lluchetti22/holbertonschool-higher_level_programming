#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] == " ":
        i += 1
    current_line = ""
    while i < len(text):
        if text[i] in ".?:":
            print(current_line.rstrip() + text[i])
            print()
            current_line = ""
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        current_line += text[i]
        i += 1
    if current_line.rstrip():
        print(current_line.rstrip(), end="")
