#!/usr/bin/env python3
from typing import Callable

"""
function that returns a function that multiplies its input by a multiplier.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def operation(number: float) -> float:
        return number * multiplier
    return operation
