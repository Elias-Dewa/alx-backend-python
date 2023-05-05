#!/usr/bin/env python3
"""The list of all the delays"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Define the list of all the delays

    Args:
        n (int): an integer number
        max_delay (int): delay to wait

    Returns:
        List[float]: list of all the delays
    """
    delay = []
    for i in range(n):
        delay.append(wait_random(max_delay))

    all_delay_list = []
    for i in asyncio.as_completed(delay):
        all_delay_list.append(await i)

    return all_delay_list
