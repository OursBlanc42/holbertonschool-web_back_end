#!/usr/bin/env python3
"""
module witch async_generator function
"""
import asyncio
import random


async def async_generator():
    """
    async_generator

    This asynchronous generator function yields random float numbers
    between 0 and 10. It waits for 1 second between each yield
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
