#!/usr/bin/env python3
"""Module that provides a function to get element lengths from an iterable."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each element in an iterable.

    Args:
        lst: Iterable containing sequences

    Returns:
        List of tuples containing each element and its length
    """
    return [(i, len(i)) for i in lst]
