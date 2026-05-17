#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if the input is None or not a string
    if not isinstance(roman_string, str):
        return 0

    # Define the integer values for each Roman symbol
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    n = len(roman_string)

    for i in range(n):
        # Get the value of the current symbol
        current_val = roman_map.get(roman_string[i], 0)
        
        # If the next symbol's value is greater, it indicates a subtraction 
        if i + 1 < n and roman_map.get(roman_string[i + 1], 0) > current_val:
            total -= current_val
        else:
            # Otherwise, add the current symbol's value
            total += current_val

    return total
