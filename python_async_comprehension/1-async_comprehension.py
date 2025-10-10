#!/usr/bin/env python3
"""Module that uses async comprehension."""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using async comprehension.

    Returns:
        List of 10 random float numbers
    """
    return [num async for num in async_generator()]
