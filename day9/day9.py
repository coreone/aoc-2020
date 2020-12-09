#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 9."""
import sys


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file) as filep:
        for line in filep:
            ret.append(int(line.rstrip()))

    return ret


def solution1(numbers, preamble=25):
    """Find solution 1."""
    cycle = 0

    for index in range(preamble, len(numbers)):
        pre_numbers = numbers[cycle:preamble+cycle]
        cycle += 1
        num = numbers[index]
        found = False
        for test in pre_numbers:
            diff = num - test
            if diff < 0:
                continue
            if diff in pre_numbers:
                found = True
                break

        if not found:
            return num

    return None


def solution2(numbers, needle):
    """Find solution 2."""
    for index, value in enumerate(numbers):
        if value > needle:
            continue
        subindex = index + 1
        found_min = value
        found_max = 0
        diff = needle - value
        while diff > 0:
            diff -= numbers[subindex]
            subindex += 1
            if numbers[subindex] < found_min:
                found_min = numbers[subindex]
            if numbers[subindex] > found_max:
                found_max = numbers[subindex]
        if diff == 0:
            return found_min + found_max

    return None


def main():
    """Execute the script."""
    numbers = get_input("input.txt")
    needle = solution1(numbers)
    print(f"Problem 1: first invalid number: {needle}")
    num = solution2(numbers, needle)
    print(f"Problem 2: weakness = {num}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
