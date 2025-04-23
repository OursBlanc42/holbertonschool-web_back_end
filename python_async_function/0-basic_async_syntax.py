#!/usr/bin/env python3
"""
This module provides an asynchronous function
to wait for a random amount of time
"""
import asyncio
import random
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """
    This function waits for a random amount of time up to the specified
    maximum delay.

    Args:
        max_delay (Union[int, float], optional): _description_. Defaults to 10.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
