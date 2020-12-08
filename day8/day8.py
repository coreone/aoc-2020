#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 7."""
import sys


class InfiniteLoopError(BaseException):
    """Raise when an infinite loop is detected."""

    def __init__(self, message, accumulator, executed):
        """Initialize the exception."""
        self.message = message
        self.accumulator = accumulator
        self.executed = executed


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file) as filep:
        for line in filep:
            data = {}
            pieces = line.rstrip().split(" ")
            data["op"] = pieces[0]
            data["val"] = pieces[1]
            ret.append(data)

    return ret


def solution1(instructions):
    """Find solution 1."""
    acc = 0
    executed = []

    index = 0
    while True:
        if index in executed:
            raise InfiniteLoopError(
                f"Inifinte loop at instruction {index}", accumulator=acc, executed=executed
            )

        executed.append(index)
        if index >= len(instructions):
            # Instructions fall out of bounds
            # print(f"out-of-bounds: {index}")
            return acc
        if instructions[index]["op"] == "nop":
            index += 1
            continue
        elif instructions[index]["op"] == "acc":
            acc = acc + int(instructions[index]["val"])
            index += 1
        elif instructions[index]["op"] == "jmp":
            index = index + int(instructions[index]["val"])

    return acc


def solution2(instructions):
    """Find solution 2."""
    acc = 0

    try:
        acc = solution1(instructions)
    except InfiniteLoopError as exc:
        executed = exc.executed

    while True:
        newinstructions = instructions.copy()
        # Get the last instruction executed
        index = executed.pop()
        if instructions[index]["op"] == "nop":
            newinstructions[index]["op"] = "jmp"
        elif instructions[index]["op"] == "jmp":
            newinstructions[index]["op"] = "nop"
        else:
            continue

        try:
            acc = solution1(newinstructions)
        except InfiniteLoopError as exc:
            pass
        else:
            return acc

    return acc


def main():
    """Execute the script."""
    instructions = get_input("input.txt")
    try:
        acc = solution1(instructions)
    except InfiniteLoopError as exc:
        acc = exc.accumulator
    print(f"Problem 1: accumulator = {acc}")
    acc = solution2(instructions)
    print(f"Problem 2: accumulator = {acc}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
