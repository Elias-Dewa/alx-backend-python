#!/usr/bin/env python3
"""Add type annotations to the function"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Union values of any type

    Args:
        dct (Mapping): dictionary
        key (Any): key
        default (Union[T, None]): default

    Returns:
        Union[Any, T]: values with the appropriate types
    """
    if key in dct:
        return dct[key]
    else:
        return default
