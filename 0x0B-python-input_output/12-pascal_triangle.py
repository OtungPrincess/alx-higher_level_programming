#!/usr/bin/python3
"""function that generates Pascal's triangle of n"""


def pascal_triangle(n):
    """Pascal's Triangle of size n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        les = triangle[-1]
        tmp = [1]
        for i in range(len(les) - 1):
            tmp.append(les[i] + les[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
