#!/usr/bin/python3
"""Module for converting Roman numerals to integers."""


def roman_to_int(roman_string):
    """Converts a Roman numeral string to an integer."""
    if not isinstance(roman_string, str):
        return 0

    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0

    for i in range(len(roman_string)):
        current = roman_values.get(roman_string[i], 0)
        if i + 1 < len(roman_string):
            next_val = roman_values.get(roman_string[i + 1], 0)
        else:
            next_val = 0

        if current < next_val:
            result -= current
        else:
            result += current

    return result
