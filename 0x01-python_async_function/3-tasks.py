#!/usr/bin/env python3
"""a function task_wait_random that takes an integer and
return a asyncio.Task"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """a function that return a asyncio.Task

    Args:
        max_delay (int): an integer number

    Returns:
        asyncio.Task: asyncio.Task
    """
    asy_task = asyncio.create_task(wait_random(max_delay))
    return asy_task
