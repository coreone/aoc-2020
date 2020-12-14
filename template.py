#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day ."""
import sys


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file) as filep:
        for line in filep:
            ret.append(int(line.rstrip()))

    return ret


def solution1(numbers):
    """Find solution 1."""

    return 0


def solution2(numbers):
    """Find solution 2."""

    return 0


def main():
    """Execute the script."""
    numbers = get_input("input.txt")
    answer = solution1(numbers)
    print(f"Problem 1: answer: {answer}")
    answer = solution2(numbers)
    print(f"Problem 2: answer = {answer}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
