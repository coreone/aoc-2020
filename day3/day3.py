#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 3."""
import sys


def get_input(file):
    """Get input from the file."""
    rows = []
    with open(file) as filep:
        for line in filep:
            rows.append(line.strip())

    return rows


def get_coord(rows, x, y):  # pylint:disable=invalid-name
    """Return 0 for open, 1 for tree at the given coordinates."""
    rowmax = len(rows[y]) - 1
    newx = x
    if x > rowmax:
        newx = x % len(rows[y])

    if rows[y][newx] == ".":
        return 0

    return 1


def traverse(rows, xslope, yslope=1):
    """Traverse the trail using the given x,y slope."""
    trees = 0
    xcoord = 0

    for row in range(yslope, len(rows), yslope):
        xcoord += xslope
        trees += get_coord(rows, xcoord, row)

    return trees


def solution1(rows):
    """Find solution 1."""
    return traverse(rows, 3, 1)


def solution2(rows):
    """Find solution 2."""
    product = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    for slope in slopes:
        res = traverse(rows, slope[0], slope[1])
        product *= res

    return product


def main():
    """Execute the script."""
    rows = get_input("input.txt")
    sol = solution1(rows)
    print(f"Problem 1: Trees encountered: {sol}")
    sol = solution2(rows)
    print(f"Problem 2: Product of trees encountered: {sol}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
