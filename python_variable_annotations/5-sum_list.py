#!/usr/bin/env python3
from typing import List

"""
function that calculates the sum of all elements in the input list
"""


def sum_list(input_list: List[float]) -> float:
    """
    function that calculates the sum of all elements in the input list
    """
    result: float = 0.0
    for item in input_list:
        result = result + item
    return result
