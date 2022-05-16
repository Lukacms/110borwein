##
## EPITECH PROJECT, 2022
## 110borwein
## File description:
## parse_args
##


from argparse import ArgumentError, ArgumentTypeError, ArgumentParser
from math import sqrt
from typing import NamedTuple
from sys import argv

from sys import exit


class Arguments(NamedTuple):
    n: int


def positive_int(arg: str) -> int:
    n: int = 0

    try:
        n = int(arg)
    except TypeError:
        raise ArgumentTypeError(f"Argument Type Error: {arg} is not an integer")
    if n < 0:
        raise ValueError(f"Value Error: {arg} must be a positive integer")
    return n


def parse_args() -> Arguments:
    parser = ArgumentParser()

    parser.add_argument(
        "n", type=positive_int, help="constant defining the integral to be computed"
    )

    try:
        args = parser.parse_args()
    except SystemExit:
        exit(84)
    return Arguments(args.n)
