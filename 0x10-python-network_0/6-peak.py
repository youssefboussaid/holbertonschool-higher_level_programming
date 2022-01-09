#!/usr/bin/python3
"""
peak function
"""

def find_peak(list_of_integers):
    len_list = len(list_of_integers)
    if list_of_integers == []:
        return None
    if len_list == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[len(list_of_integers) - 1] >= list_of_integers[len(list_of_integers) - 2]:
        return list_of_integers[len(list_of_integers) - 1]
    for i in range(1, len(list_of_integers) - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]
