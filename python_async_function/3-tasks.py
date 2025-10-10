#!/usr/bin/env python3
"""Module that creates asyncio Tasks."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio Task for wait_random.

    Args:
        max_delay: Maximum delay for wait_random

    Returns:
        asyncio.Task object
    """
    return asyncio.create_task(wait_random(max_delay))
