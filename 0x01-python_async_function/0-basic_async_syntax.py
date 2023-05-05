#!/usr/bin/env python3
"""an asynchronous coroutine"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """a function that waits for a random delay between 0 and max_delay

    Args:
        max_delay (int, optional): an integer number. Defaults to 10.

    Returns:
        float: a random delay between 0 and max_delay
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
