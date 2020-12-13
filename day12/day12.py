#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 12."""
import logging
import os
import sys

LOGGER = logging.getLogger(os.path.basename(__file__))


class Waypoint():
    """Waypoint class."""

    def __init__(self, xoffset, yoffset):
        """Initialize the class."""
        self.xoffset = xoffset
        self.yoffset = yoffset
        # LOGGER.debug("Waypoint: xoffset=%s, yoffset=%s", self.xoffset, self.yoffset)

    @property
    def xcompass(self):
        """Return what the x direction compass would be."""
        compass = 90
        if self.xoffset < 0:
            compass = 270

        return compass

    @property
    def ycompass(self):
        """Return what the y direction compass would be."""
        compass = 0
        if self.yoffset < 0:
            compass = 180

        return compass

    def rotate(self, command):
        """Rotate the waypoint around the ship."""
        xcompass = self.xcompass
        ycompass = self.ycompass
        # LOGGER.debug("Waypoint(rotate): xcompass=%s, ycompass=%s", xcompass, ycompass)
        # LOGGER.debug("Waypoint(rotate): xoffset=%s, yoffset=%s", self.xoffset, self.yoffset)
        xcompass, xadjx, xadjy = orientation(xcompass, command)
        ycompass, yadjx, yadjy = orientation(ycompass, command)
        # LOGGER.debug("Waypoint(rotate): xcompass=%s, xadjx=%s, xadjy=%s", xcompass, xadjx, xadjy)
        # LOGGER.debug("Waypoint(rotate): ycompass=%s, yadjx=%s, yadjy=%s", ycompass, yadjx, yadjy)
        newxoffset = (xadjx * abs(self.xoffset)) + (yadjx * abs(self.yoffset))
        newyoffset = (xadjy * abs(self.xoffset)) + (yadjy * abs(self.yoffset))
        self.xoffset = newxoffset
        self.yoffset = newyoffset
        # LOGGER.debug("Waypoint(rotate): xoffset=%s, yoffset=%s", self.xoffset, self.yoffset)

    def move(self, command):
        """Move the waypoint."""
        # LOGGER.debug("Waypoint(move): xoffset=%s, yoffset=%s", self.xoffset, self.yoffset)
        orig = self.xoffset
        self.xoffset += command["xval"]
        orig = self.yoffset
        self.yoffset += command["yval"]
        # LOGGER.debug("Waypoint(move): xoffset=%s, yoffset=%s", self.xoffset, self.yoffset)


def get_input(file):
    """Get formatted input from the file."""
    directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

    ret = []
    with open(file) as filep:
        for line in filep:
            line = line.rstrip()
            tmp = {}
            tmp["action"] = line[0:1]
            tmp["value"] = int(line[1:])
            if tmp["action"] in directions:
                tmp["xval"] = tmp["value"] * directions[tmp["action"]][0]
                tmp["yval"] = tmp["value"] * directions[tmp["action"]][1]
            ret.append(tmp)

    return ret


def adjust_compass(compass, command):
    """Adjust the compass heading."""
    degrees = command["value"]
    if command["action"] == "L":
        degrees *= -1

    newcoord = compass + degrees
    newcoord = abs(newcoord % 360)

    return newcoord


def orientation(compass, change):
    """Change the orientation of the ship."""
    newcoord = adjust_compass(compass, change)

    coordsign = 1
    if newcoord > 90:
        coordsign = -1

    if (newcoord % 180) == 0:
        newx = 0
        newy = 1 * coordsign
    else:
        newx = 1 * coordsign
        newy = 0

    return (newcoord, newx, newy)


def solution1(directions):
    """Find solution 1."""
    compass = 90
    x_dir = 1
    y_dir, x_coord, y_coord = 0, 0, 0
    for command in directions:
        if command["action"] in ["R", "L"]:
            compass, x_dir, y_dir = orientation(compass, command)
        elif command["action"] == "F":
            x_coord += x_dir * command["value"]
            y_coord += y_dir * command["value"]
        else:
            x_coord += command["xval"]
            y_coord += command["yval"]

    return abs(x_coord) + abs(y_coord)


def solution2(directions):
    """Find solution 2."""
    waypoint = Waypoint(10, 1)
    x_coord, y_coord = 0, 0
    for command in directions:
        # LOGGER.debug("solution2: command: %s", str(command))
        # LOGGER.debug("solution2: ship: %s, %s", x_coord, y_coord)
        if command["action"] in ["R", "L"]:
            # LOGGER.debug("solution2: command: %s", str(command))
            waypoint.rotate(command)
        elif command["action"] == "F":
            x_coord += waypoint.xoffset * command["value"]
            y_coord += waypoint.yoffset * command["value"]
        else:
            waypoint.move(command)
        # LOGGER.debug("solution2: final ship: %s, %s", x_coord, y_coord)

    return abs(x_coord) + abs(y_coord)


def main():
    """Execute the script."""
    # logging.basicConfig(level="DEBUG")
    directions = get_input("input.txt")
    distance = solution1(directions)
    print(f"Problem 1: Manhattan distance: {distance}")
    occupied = solution2(directions)
    print(f"Problem 2: Manhattan distance: {occupied}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
