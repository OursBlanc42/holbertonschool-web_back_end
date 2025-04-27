#!/usr/bin/env python3
"""
module witch measure_time function
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures runtime of executing four
    instances of async_comprehension concurrently.
    """
    start = time.perf_counter()
    _ = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())

    end = time.perf_counter()

    return (end - start)
