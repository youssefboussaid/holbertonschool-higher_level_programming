#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False:
        return 0
    elif not roman_string:
        return 0
    else:
        value = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
 
    # Initialize previous character and answer
    p = 0
    ans = 0
 
    # Traverse through all characters
    n = len(roman_string)
    for i in range(n-1, -1, -1):
 
        # If greater than or equal to previous,
        # add to answer
        if value[roman_string[i]] >= p:
            ans += value[roman_string[i]]
 
        # If smaller than previous
        else:
            ans -= value[roman_string[i]]
 
        # Update previous
        p = value[roman_string[i]]
    return(ans)
