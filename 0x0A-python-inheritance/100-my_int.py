#!/usr/bin/python3
"""
MyInt module 
"""

class MyInt(int):
    """
    MyInt class
    """
    def __eq__(self, value):
        """ equal"""
        return not super().__eq__(value)
    def __ne__(self, value):
        """ diffrent """
        return not super().__ne__(value)
