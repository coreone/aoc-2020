#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 10."""
import sys


def get_sorted_input(file):
    """Get formatted input from the file."""
    ret = []
    # Account for the initial difference between the outlet and the adapter
    ret.append(0)

    with open(file) as filep:
        for line in filep:
            num = int(line.rstrip())
            if not ret:
                ret.append(num)
            else:
                for index, value in enumerate(ret):
                    if num < value:
                        ret.insert(index, num)
                        break
                    if index == (len(ret) - 1):
                        ret.append(num)
                        break

    # Get the last element so we can account for the difference between the last
    # adapter and the device
    last = ret.pop()
    ret.append(last)
    ret.append(last+3)

    return ret


def find_diffs(adapters):
    """Find the differences between all outlets."""
    diffs = {}

    for index in range(1, len(adapters)):
        diff = adapters[index] - adapters[index-1]
        if diff not in diffs:
            diffs[diff] = 1
        else:
            diffs[diff] += 1

    return diffs


def solution1(adapters):
    """Find solution 1."""
    diffs = find_diffs(adapters)

    return diffs[1] * diffs[3]


def solution2(adapters):
    """Find solution 2."""
    arrangement = 0

    return arrangement


def main():
    """Execute the script."""
    adapters = get_sorted_input("input.txt")
    diffs = solution1(adapters)
    print(f"Problem 1: {diffs} differences")
    arrangement = solution2(adapters)
    print(f"Problem 2: {arrangement} arrangements")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
