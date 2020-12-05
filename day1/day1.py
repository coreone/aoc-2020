#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 1."""
import sys


def get_numbers(file):
    """Get numbers from the file."""
    nums = {}
    with open(file) as filep:
        for line in filep:
            num = int(line.strip())
            nums[num] = num

    return nums


def solution1(nums):
    """Find the solution."""
    for num in nums:
        num2 = 2020 - num
        if num2 in nums:
            return (num, num2)


def solution2(nums):
    """Find the solution."""
    for num in nums:
        for num2 in nums:
            if num == num2:
                continue
            thesum = num + num2
            if thesum < 2020:
                num3 = 2020 - thesum
                if num3 in nums:
                    return (num, num2, num3)


def main():
    """Execute the script."""
    nums = get_numbers("input.txt")
    sol = solution1(nums)
    print(f"Problem 1: {sol[0]} * {sol[1]} = {sol[0] * sol[1]}")
    sol = solution2(nums)
    print(f"Problem 2: {sol[0]} * {sol[1]} * {sol[2]} = {sol[0] * sol[1] * sol[2]}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
