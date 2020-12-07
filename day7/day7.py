#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 7."""
import sys


def get_input(file):
    """Get formatted input from the file."""
    ret = {}
    with open(file) as filep:
        for line in filep:
            pieces = line.rstrip().split(" ")
            main_pattern = f"{pieces[0]} {pieces[1]}"
            ret[main_pattern] = {}
            section = 4
            while True:
                if (len(pieces) <= section) or not pieces[section].isnumeric():
                    break

                sub_pattern = f"{pieces[section+1]} {pieces[section+2]}"
                ret[main_pattern][sub_pattern] = int(pieces[section])
                section += 4

    return ret


def fill_bag(bags, bag):
    """Recursively fill bag."""
    ret = []

    if not bags[bag]:
        return []

    for subbag in bags[bag]:
        ret += [subbag] + fill_bag(bags, subbag)

    return ret


def solution1(bags):
    """Find solution 1."""
    count = 0
    for bag in bags:
        if not bags[bag]:
            continue
        allbags = fill_bag(bags, bag)
        if "shiny gold" in allbags:
            count += 1

    return count


def solution2(bags, bag="shiny gold"):
    """Find solution 2."""
    total = 0

    if not bags[bag]:
        return 0

    for subbag in bags[bag]:
        total += (solution2(bags, subbag) * bags[bag][subbag]) + bags[bag][subbag]

    return total


def main():
    """Execute the script."""
    bags = get_input("input.txt")
    valid = solution1(bags)
    print(f"Problem 1: {valid} bags")
    valid = solution2(bags)
    print(f"Problem 2: {valid} bags")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
