#!/usr/bin/env python3
"""Write a type-annotated function - sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum a list of float values

    Args:
          input_list (float): a number

      Returns:
          float: the sum of the list of float values
    """
    return sum(input_list)
