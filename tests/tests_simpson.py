##
## EPITECH PROJECT, 2022
## 110borwein
## File description:
## tests_simpson
##

from unittest import TestCase
from src.midpoint.midpoint import midpoint
from src.trapezoidal.trapezoidal import trapezoidal
from src.simpson.simpson import simpson


class tests_trapezoidal(TestCase):
    def test_trapezoidal(self):
        constant: int = 5
        rmidpoint: float = midpoint(constant)
        rtrapezoidal: float = trapezoidal(constant)
        res: float = 1.5707963268

        self.assertAlmostEqual(simpson(rmidpoint, rtrapezoidal), res)
