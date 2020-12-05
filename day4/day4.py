#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 4."""
import logging
import os
import sys

LOGGER = logging.getLogger(os.path.basename(__file__))


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


def validate_range(val, low, high):
    """Validate integer field."""
    int_val = int(val)
    if (int_val >= low) and (int_val <= high):
        return True

    LOGGER.info("integer out of range: %s (%s, %s)", val, low, high)
    return False


def validate_byr(val):
    """Validate byr field."""
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    return validate_range(val, 1920, 2002)


def validate_iyr(val):
    """Validate iyr field."""
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    return validate_range(val, 2010, 2020)


def validate_eyr(val):
    """Validate eyr field."""
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    return validate_range(val, 2020, 2030)


def validate_hgt(val):
    """Validate hgt field."""
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    if val.endswith("cm"):
        tmp = int(val.rstrip("cm"))
        if validate_range(tmp, 150, 193):
            return True
    elif val.endswith("in"):
        tmp = int(val.rstrip("in"))
        if validate_range(tmp, 59, 76):
            return True

    LOGGER.info("invalid hgt: %s", val)
    return False


def validate_hcl(val):
    """Validate hcl field."""
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if val.startswith("#"):
        tmp = val.lstrip("#").lower()
        count = 0
        for char in tmp:
            count += 1
            # Validate ascii between 0-9 and a-f
            if not validate_range(ord(char), 48, 57) and not validate_range(ord(char), 97, 102):
                return False

        if count == 6:
            return True

    LOGGER.info("invalid hcl: %s", val)
    return False


def validate_ecl(val):
    """Validate ecl field."""
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if val in colors:
        return True

    LOGGER.info("invalid ecl: %s", val)
    return False


def validate_pid(val):
    """Validate hgt field."""
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    count = 0
    for char in val:
        count += 1
        if not validate_range(ord(char), 48, 57):
            return False

    if count == 9:
        return True

    LOGGER.info("invalid pid: %s", val)
    return False


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
            LOGGER.warning("Invalid passport: %s" % str(passport))
            LOGGER.warning("Missing fields: %s" % ", ".join(fields))
        else:
            count += 1

    return count


def solution2(passports):
    """Find solution 2."""
    allowed_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    required_fields = allowed_fields.copy()
    required_fields.remove("cid")

    count = 0
    for passport in passports:
        fields = required_fields.copy()
        for field in passport:
            if field != "cid":
                try:
                    if globals()[f"validate_{field}"](passport[field]):
                        fields.remove(field)
                except Exception as exc:
                    LOGGER.info(f"{field} is invalid: {passport[field]}")
        if fields:
            LOGGER.warning("Invalid passport: %s" % str(passport))
        else:
            count += 1

    return count


def main():
    """Execute the script."""
    logging.basicConfig(level="ERROR")
    passports = get_input("input.txt")
    sol = solution1(passports)
    print(f"Problem 1: {sol} valid passports")
    sol = solution2(passports)
    print(f"Problem 2: {sol} valid passports")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
