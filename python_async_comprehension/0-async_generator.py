#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Async generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


if __name__ == "__main__":

    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result, len(result))

    asyncio.run(print_yielded_values())
