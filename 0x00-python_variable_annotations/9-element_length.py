#!/usr/bin/env python3
"""Annotate the below function’s parameters
"""

from typing import List, Union, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the function

    Args:
        lst (Iterable[Sequence]): Iterable sequence list

    Returns:
        List[Tuple[Sequence, int]]: values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
