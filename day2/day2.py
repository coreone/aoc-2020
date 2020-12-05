#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 2."""
import re
import sys


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file) as filep:
        for line in filep:
            data = {}
            pieces = re.split(r"[- :]", line.strip())
            data["min"] = int(pieces[0])
            data["max"] = int(pieces[1])
            data["char"] = pieces[2]
            data["password"] = pieces[4]

            ret.append(data)

    return ret


def solution(data):
    """Find solution 1."""
    bad = 0
    count = 0
    for datum in data:
        count += 1
        lmin = 0
        lmax = datum["max"]
        for letter in datum["password"]:
            if letter == datum["char"]:
                lmin += 1
                lmax -= 1

        if (lmin < datum["min"]) or (lmax < 0):
            bad += 1

    return count - bad


def solution2(data):
    """Find solution 2."""
    bad = 0
    count = 0
    for datum in data:
        count += 1
        found = 0
        if datum["password"][datum["min"]-1] == datum["char"]:
            found += 1
        if datum["password"][datum["max"]-1] == datum["char"]:
            found += 1
        if found != 1:
            bad += 1

    return count - bad


def main():
    """Execute the script."""
    data = get_input("input.txt")
    valid = solution(data)
    print(f"Problem 1: {valid} valid passwords")
    valid = solution2(data)
    print(f"Problem 2: {valid} valid passwords")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
