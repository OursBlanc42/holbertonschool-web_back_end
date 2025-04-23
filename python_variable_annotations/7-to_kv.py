#!/usr/bin/env python3
from typing import Union, Tuple

"""
function that returns a tuple with the string and the square of the number
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v * v)
