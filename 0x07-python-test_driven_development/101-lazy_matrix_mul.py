#!/usr/bin/python3
"""
Function that multiplies 2 matricies using numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies 2 given matrix
    """
    return numpy.matmul(m_a, m_b)
