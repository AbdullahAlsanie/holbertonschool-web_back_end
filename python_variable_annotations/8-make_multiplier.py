#!/usr/bin/env python3
"""Module that provides a function to create a multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier: The multiplier value

    Returns:
        A function that takes a float and returns it multiplied by multiplier
    """
    def multiply(n: float) -> float:
        """Multiply a number by the multiplier.

        Args:
            n: Number to multiply

        Returns:
            The product of n and multiplier
        """
        return n * multiplier
    return multiply
