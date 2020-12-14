#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 14."""
import sys
# import pdb


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file) as filep:
        inst_set = {}
        for line in filep:
            if line.startswith("mask"):
                if inst_set:
                    ret.append(inst_set)
                    inst_set = {}
                inst_set["mask"], inst_set["maskand"], inst_set["maskor"] = parse_mask(line)
                inst_set["instructions"] = []
            else:
                inst_set["instructions"].append(parse_instruction(line))

        ret.append(inst_set)

    return ret


def parse_mask(line):
    """Parse the bit mask from input."""
    maskand = 0
    maskor = 0

    pieces = line.split("=")
    mask = pieces[1].strip()
    maskand, maskor = generate_bitmasks(mask)

    # print(mask)
    # print(f"{maskand:>36b} # maskand")
    # print(f"{maskor:>36b} # maskor")
    return (mask, maskand, maskor)


def generate_bitmasks(mask, ors="1", ands="X"):
    """Parse the bit mask from input."""
    maskand = 0
    maskor = 0

    power = 0
    for index in range(len(mask) - 1, -1, -1):
        factor = 2 ** power
        if mask[index] == ors:  # 1
            maskor += factor
            maskand += factor
        elif mask[index] == ands:  # X
            maskand += factor
        power += 1

    return (maskand, maskor)


def parse_instruction(line):
    """Parse the bit mask from input."""
    ret = {}
    pieces = line.split("=")
    ret["value"] = int(pieces[1].strip())
    ret["mem"] = int(pieces[0].replace("mem[", "").replace("]", ""))

    return ret


def generate_masks(mask, index=0):
    """Parse the bit mask from input."""
    masks = []

    if index >= len(mask):
        _, tmpmask = generate_bitmasks(mask, ors="1", ands="")
        masks.append(tmpmask)
        # print(f"{tmpmask:>36b}")
        return masks

    factor = 2 ** ((len(mask) - 1) - index)
    allmasks = generate_masks(mask, index+1)
    masks = allmasks.copy()
    if mask[index] == "X":
        for tmpmask in allmasks:
            # print(f"{tmpmask:>36b}")
            masks.append(tmpmask | factor)
        # pdb.set_trace()

    return masks


def solution1(inst_sets):
    """Find solution 1."""
    memory = {}
    for section in inst_sets:
        maskand = section["maskand"]
        maskor = section["maskor"]
        for inst in section["instructions"]:
            # print(inst)
            index = inst["mem"]
            memory[index] = inst["value"] & maskand
            # print(memory)
            memory[index] = memory[index] | maskor
            # print(memory)
            # print()

    # print(memory)
    total = 0
    for pos in memory:
        total += memory[pos]

    return total


def solution2(inst_sets):
    """Find solution 2."""
    for section in inst_sets:
        print(f"{section['mask']}")
        masks = generate_masks(section["mask"], section["maskor"])
        for inst in section["instructions"]:
            index = inst["mem"]
            for mask in masks:
                newindex = index & mask
                print(index)
                print(f"index: {index:>36b}")
                print(f"mask:  {mask:>36b}")
                print(f"new:   {newindex:>36b}")
                print(newindex)
                # memory[index] = inst["value"] & maskand
                # pdb.set_trace()

    return 0


def main():
    """Execute the script."""
    # inst_sets = get_input("input.txt")
    inst_sets = get_input("test2.txt")
    answer = solution1(inst_sets)
    print(f"Problem 1: answer: {answer}")
    # return 0
    answer = solution2(inst_sets)
    print(f"Problem 2: answer = {answer}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
