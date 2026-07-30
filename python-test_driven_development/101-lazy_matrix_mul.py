#!/usr/bin/python3
"""
Defines a matrix multiplication function using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        ndarray: The matrix result of the multiplication.
    """
    return np.matmul(m_a, m_b)
