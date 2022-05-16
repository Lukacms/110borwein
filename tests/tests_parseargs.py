##
## EPITECH PROJECT, 2022
## 110borwein
## File description:
## general_tests
##

import unittest
import sys
from unittest.mock import patch
from src.parse_args import parse_args, Arguments


class test_parse_args(unittest.TestCase):
    def test_parseargs(self):
        testargs: list[str] = ["./110borwein", "5"]
        args: Arguments = Arguments(5)

        with patch.object(sys, "argv", testargs):
            self.assertEqual(parse_args().n, args.n)

    def test_parseargs_false(self):
        testargs: list[str] = ["./110borwein", "5"]
        args: Arguments = Arguments(5645)

        with patch.object(sys, "argv", testargs):
            self.assertNotEqual(parse_args().n, args.n)
