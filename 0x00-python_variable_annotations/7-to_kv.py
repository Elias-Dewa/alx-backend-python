#!/usr/bin/env python3
"""Write a type-annotated function - to_kv"""

from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert string and an int OR float to a tuple

    Args:
        k (str): A string
        v (Union[int, float]): list of union of integers and floats

    Returns:
        Tuple: a tuple
    """
    return (k, v * v)
