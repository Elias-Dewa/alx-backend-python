#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplies a float by multiplier

    Args:
        multiplier (float): a float multiplier

    Returns:
        Callable[[float], float]: a function that multiplies 
        a float by multiplier
    """
    def mul_fun(n: float):
        return n * multiplier
    return mul_fun
