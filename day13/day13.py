#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 13."""
import sys


def get_input(file):
    """Get formatted input from the file."""
    ret = {"timestamp": 0, "buses": {}}
    count = 0
    with open(file) as filep:
        ret["timestamp"] = int(filep.readline().rstrip())
        notes = filep.readline().rstrip()
        pieces = notes.split(",")
        bus = None
        for val in pieces:
            if val.isnumeric():
                bus = int(val)
                ret["buses"][bus] = {
                    "count": count,
                    "x": [],
                }
            else:
                ret["buses"][bus]["x"].append(val)
            count += 1

    return ret


def solution1(schedule_data):
    """Find solution 1."""
    timestamp = schedule_data["timestamp"]
    found = 0
    while not found:
        for bus in schedule_data["buses"]:
            if timestamp % bus == 0:
                found = timestamp - schedule_data["timestamp"]
                break
        if not found:
            timestamp += 1

    return found * bus


def solution2_infinity(schedule_data):
    """Find solution 2."""
    first_bus = list(schedule_data["buses"].keys())[0]
    first_timestamp = schedule_data["timestamp"]
    while True:
        if first_timestamp % first_bus == 0:
            break
        first_timestamp += 1

    timestamp = first_timestamp
    num_buses = len(schedule_data["buses"])
    found = 0
    while found < num_buses:
        for bus in schedule_data["buses"]:
            tmpts = timestamp + schedule_data["buses"][bus]["count"]
            if tmpts % bus == 0:
                found += 1

        if found < num_buses:
            found = 0
            timestamp += first_bus

    return timestamp


def main():
    """Execute the script."""
    schedule_data = get_input("input.txt")
    schedule_data = get_input("test7.txt")
    product = solution1(schedule_data)
    print(f"Problem 1: bus product: {product}")
    timestamp = solution2_infinity(schedule_data)
    print(f"Problem 2: timestamp = {timestamp}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
