#!/usr/bin/python3
"""
Module to divide all elements of matrix
"""


def matrix_divided(matrix, div):
    """
   function that divides all elements of a matrix.
   Args:
       matrix(list of lists of integers or floats): to be divided matrix
       div(int/float): the number that divides the matrix
   Raises:
       TypeError:  -if matrix is not a list of integers/floats
                   -Each row of the matrix must have the same size
                   -if div is not of type int or float
       ZeroDivisionError: when div equal to 0
   Returns:
       new matrix
   """

    if not  isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, (list, float, int)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for i in range(0, len(matrix)):
        n_matrix = []
        for j in matrix[i]:
            n_matrix.append(round((j / div), 2))
        new_matrix.append(n_matrix)
    return new_matrix
