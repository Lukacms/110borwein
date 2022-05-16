##
## EPITECH PROJECT, 2022
## 110borwein
## File description:
## trapezoidal
##

from src.borwein import Borwein


def trapezoidal(constant: int) -> float:
    borwein: Borwein = Borwein(constant)
    result: float = 0.0
    i: float = 0.0

    while i < 5000:
        result += (i + 0.5 - i) * (borwein(i) + borwein(i + 0.5)) / 2
        i += 0.5
    return result
