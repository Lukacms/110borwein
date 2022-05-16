##
## EPITECH PROJECT, 2022
## 110borwein
## File description:
## print_results
##

from math import pi


def print_result(midpoint: float, trapezoidal: float, simpson: float, n: int) -> None:
    m_diff: float = abs((pi / 2) - midpoint)
    t_diff: float = abs((pi / 2) - trapezoidal)
    s_diff: float = abs((pi / 2) - simpson)

    print("Midpoint:")
    print(f"I{n} = {midpoint:.10f}")
    print(f"diff = {m_diff:.10f}\n")

    print("Trapezoidal:")
    print(f"I{n} = {trapezoidal:.10f}")
    print(f"diff = {t_diff:.10f}\n")

    print("Simpson:")
    print(f"I{n} = {simpson:.10f}")
    print(f"diff = {s_diff:.10f}")
