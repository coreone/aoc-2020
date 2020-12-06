#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 6."""
import sys


def get_input(file):
    """Get input from the file."""
    answers = []
    currgroup = []

    with open(file) as filep:
        for line in filep:
            line = line.strip()
            if not line:
                answers.append(currgroup)
                currgroup = []
                continue

            currgroup.append(line)

        # Catch the last line if the file doesn't end with a newline!!!
        if currgroup:
            answers.append(currgroup)

    return answers


def solution1(answers):
    """Find solution 1."""
    count = 0

    for group in answers:
        found = []
        for person in group:
            for question in person:
                if question not in found:
                    found.append(question)
        count += len(found)

    return count


def solution2(answers):
    """Find solution 2."""
    count = 0

    for group in answers:
        found = {}
        for person in group:
            for question in person:
                if question not in found:
                    found[question] = 1
                else:
                    found[question] += 1

            for question in found:
                if found[question] == len(group):
                    count += 1

    return count


def main():
    """Execute the script."""
    answers = get_input("input.txt")
    sol = solution1(answers)
    print(f"Problem 1: Total answers: {sol}")
    sol = solution2(answers)
    print(f"Problem 2: Total common answers: {sol}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
