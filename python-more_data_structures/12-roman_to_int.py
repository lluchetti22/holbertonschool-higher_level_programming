#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    length = len(roman_string)
    
    for i in range(length):
        current_val = roman_map.get(roman_string[i], 0)
        
        # Check if a next character exists and if it is larger than the current one
        if i + 1 < length and current_val < roman_map.get(roman_string[i + 1], 0):
            total -= current_val
        else:
            total += current_val
            
    return total
