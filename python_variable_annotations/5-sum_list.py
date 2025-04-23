#!/usr/bin/env python3
from typing import List


def sum_list(input_list: List[float]) -> float:
    result: float = 0.0
    for item in input_list:
        result = result + item
    return result
