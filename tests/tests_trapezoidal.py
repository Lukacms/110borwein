##
## EPITECH PROJECT, 2022
## 110borwein
## File description:
## tests_trapezoidal
##

from unittest import TestCase
from src.trapezoidal.trapezoidal import trapezoidal


class tests_trapezoidal(TestCase):
    def test_trapezoidal(self):
        constant: int = 5
        res: float = 1.5707963268

        self.assertAlmostEqual(trapezoidal(constant), res)
