##
## EPITECH PROJECT, 2022
## 110borwein
## File description:
## borwein
##

from math import sin


class Borwein:
    def __init__(self, n: int):
        self.n: int = int(n)

    def __call__(self, x: float) -> float:
        result: float = 1.0

        if x == 0:
            return 1
        for k in range(0, self.n + 1):
            x_ = x / (2 * k + 1)
            result = result * sin(x_) / x_
        return result
