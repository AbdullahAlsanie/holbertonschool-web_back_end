#!/usr/bin/env python3
"""Module that provides a function to sum a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculate the sum of a list of floats.

    Args:
        input_list: List of float numbers to sum

    Returns:
        The sum of all floats in the list
    """
    return sum(input_list)
