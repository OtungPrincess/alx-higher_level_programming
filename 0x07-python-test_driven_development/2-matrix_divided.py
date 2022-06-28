#!/usr/bin/python3
"""
Module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix
    """

    err_1 = "matrix must be a matrix (list of lists) of integers/floats"
    err_2 = "Each row of the matrix must have the same size"
    divide_1 = "div must be a number"
    division_2 = "division by zero"

    if not type(div) in (float, int):
        raise TypeError(divide_1)
    if div == 0:
        raise ZeroDivisionError(division_2)

    if not type(matrix) is (list) or len(matrix) == 0:
        raise TypeError(err_1)
    for array in matrix:
        if not type(array) is (list):
            raise TypeError(err_1)

        if len(matrix[0]) is not len(array):
            raise TypeError(err_2)
        for new in array:
            if not type(new) in (float, int):
                raise TypeError(err_1)

    return[[round(new / div, 2) for new in i] for i in matrix]
