#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Union values of any type

    Args:
        lst (Sequence[Any]]): any sequence

    Returns:
        Union[Any, None]: values with the appropriate types
    """
    if lst:
        return lst[0]
    else:
        return None
