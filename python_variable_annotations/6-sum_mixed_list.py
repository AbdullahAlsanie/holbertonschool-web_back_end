#!/usr/bin/env python3
"""Module that provides a function to sum a mixed list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculate the sum of a list containing integers and floats.

    Args:
        mxd_lst: List of integers and floats to sum

    Returns:
        The sum of all numbers in the list as a float
    """
    return sum(mxd_lst)
