#!/usr/bin/env python3
"""Coroutine async_generator that takes no arguments.

The coroutine loops 10 times, each time asynchronously waits 1 second,
then yields a random number between 0 and 10. Use the random module.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times, wait 1 sec each time"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
