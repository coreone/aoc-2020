#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 11."""
# import logging
# import os
import sys

# LOGGER = logging.getLogger(os.path.basename(__file__))


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file) as filep:
        for line in filep:
            arr = []
            for char in line.rstrip():
                arr.append(char)
            ret.append(arr)

    return ret


def check_slope(seats, seat_x, seat_y, slope_x, slope_y, limit=1):
    """Check the provided slope."""
    step = 0

    # LOGGER.debug("check_slope: %s, %s (%s, %s) (%s)", seat_x, seat_y, slope_x, slope_y, limit)
    while step < limit:
        step += 1
        ycoord = seat_y + (step * slope_y)
        xcoord = seat_x + (step * slope_x)
        # LOGGER.debug("check_slope: step %s (%s, %s)", step, xcoord, ycoord)

        if (ycoord < 0) or (ycoord >= len(seats)):
            # LOGGER.debug("check_slope: y(%s) out of bounds", ycoord)
            return 0
        if (xcoord < 0) or (xcoord >= len(seats[seat_y])):
            # LOGGER.debug("check_slope: x(%s) out of bounds", xcoord)
            return 0
        if seats[ycoord][xcoord] == "L":
            # LOGGER.debug("check_slope: unoccupied found at %s,%s", xcoord, ycoord)
            return 0
        if seats[ycoord][xcoord] == "#":
            # LOGGER.debug("check_slope: occupied found at %s,%s", xcoord, ycoord)
            return 1

    return 0


def occupied_seats(seats, seat_x, seat_y, limit=1):
    """Determine if a seat is 'empty'."""
    occupied = 0

    # LOGGER.debug("occupied_seats: %s, %s (%s)", seat_x, seat_y, limit)
    for y_slope in range(-1, 2):
        for x_slope in range(-1, 2):
            # LOGGER.debug("occupied_seats: slope(%s, %s)", x_slope, y_slope)
            if (x_slope == 0) and (y_slope == 0):
                # LOGGER.debug("occupied_seats: skip x/y coordinate")
                continue
            occupied += check_slope(seats, seat_x, seat_y, x_slope, y_slope, limit)

    # LOGGER.debug("occupied_seats: %s occupied", occupied)
    return occupied


def seating_pass(seats, leave_count=4, limit=1):
    """Do a pass through seating to change occupancy."""
    newseats = []
    changes = 0

    for seat_y, row in enumerate(seats):
        newseats.append([])
        for seat_x, value in enumerate(row):
            newseats[seat_y].append(value)
            if value == ".":
                continue
            count = occupied_seats(seats, seat_x, seat_y, limit)
            if count == 0:
                newseats[seat_y][seat_x] = "#"
                if value != "#":
                    changes += 1
            elif count >= leave_count:
                newseats[seat_y][seat_x] = "L"
                if value != "L":
                    changes += 1

    return (changes, newseats)


def solution1(seats, leave_count=4, limit=1):
    """Find solution 1."""
    count = 0
    newseats = seats.copy()

    while True:
        changes, newseats = seating_pass(newseats, leave_count, limit)
        if changes == 0:
            break

    for row in newseats:
        for _, value in enumerate(row):
            if value == "#":
                count += 1

    return count


def solution2(seats):
    """Find solution 2."""
    return solution1(seats, leave_count=5, limit=len(seats))


def main():
    """Execute the script."""
    # logging.basicConfig(level="ERROR")
    seats = get_input("input.txt")
    occupied = solution1(seats)
    print(f"Problem 1: occupied seats: {occupied}")
    occupied = solution2(seats)
    print(f"Problem 2: occupied seats: {occupied}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
