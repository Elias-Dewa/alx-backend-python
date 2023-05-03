#!/usr/bin/env python3
"""Write a type-annotated function - sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum as a float

    Args:
        mxd_lst (List[Union[int, float]]): list of integers and floats

    Returns:
        float: their sum as a float.
    """
    return sum(mxd_lst)
