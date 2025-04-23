#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    result: float = 0.0
    for item in mxd_list:
        result = result + item
    return result
