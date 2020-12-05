#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 4."""
import sys


def process_line(line):
    """Process a line of data."""
    data = {}
    for piece in map(lambda x: x.split(":"), line.split(" ")):
        data[piece[0]] = piece[1]

    return data


def get_input(file):
    """Get input from the file."""
    passports = []
    currpass = {}

    with open(file) as filep:
        for line in filep:
            line = line.strip()
            if not line:
                passports.append(currpass)
                currpass = {}
                continue

            newdata = process_line(line)
            currpass.update(newdata)

        # Catch the last line if the file doesn't end with a newline!!!
        if currpass:
            passports.append(currpass)

    return passports


def solution1(passports):
    """Find solution 1."""
    allowed_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    required_fields = allowed_fields.copy()
    required_fields.remove("cid")

    count = 0
    for passport in passports:
        fields = required_fields.copy()
        for field in passport:
            if field != "cid":
                fields.remove(field)

        if fields:
            print("Invalid passport: %s" % str(passport))
            print("Missing fields: %s" % ", ".join(fields))
        else:
            count += 1

    return count


def solution2(passports):
    """Find solution 2."""
    return 0


def main():
    """Execute the script."""
    passports = get_input("input.txt")
    # for p in passports:
    #     print(p)
    # return 0
    # import pdb
    # pdb.set_trace()
    sol = solution1(passports)
    print(f"Problem 1: {sol} valid passports")
    # sol = solution2(passports)
    # print(f"Problem 2: {sol}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
