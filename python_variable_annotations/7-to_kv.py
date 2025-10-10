#!/usr/bin/env python3
"""Module that provides a function to create a tuple from string and number."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple with a string and the square of a number.

    Args:
        k: String key
        v: Integer or float value to be squared

    Returns:
        Tuple containing the string and the square of v as a float
    """
    return (k, v ** 2)
