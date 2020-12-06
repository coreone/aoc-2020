#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 5."""
import sys


def get_input(file):
    """Get formatted input from the file."""
    ret = {}
    with open(file) as filep:
        for line in filep:
            data = parse_id_bitwise(line.strip())
            ret[data["seat_id"]] = data

    return ret


def parse_id(ticket_id):
    """Parse the ticket ID into its values."""
    data = {}
    data["ticket_id"] = ticket_id

    row = ticket_id[0:7].replace("F", "0").replace("B", "1")
    seat = ticket_id[7:10].replace("R", "1").replace("L", "0")
    data["row"] = int(row, 2)
    data["seat"] = int(seat, 2)
    data["seat_id"] = (data["row"] * 8) + data["seat"]

    return data


def parse_id_bitwise(ticket_id):
    """Parse the ticket ID into its values (bitwise)."""
    data = {}
    data["ticket_id"] = ticket_id

    data["seat_id"] = 0
    for col in range(0, 10):
        if ticket_id[col] in ["B", "R"]:
            # Shift is directly opposite to column
            data["seat_id"] += (1 << (9 - col))

    # Need to >> 3 to throw away the seat bits
    data["row"] = (data["seat_id"] & 0b1111111000) >> 3
    data["seat"] = data["seat_id"] & 0b0000000111

    return data


def solution1(tickets):
    """Find solution 1."""
    min_id = 0
    max_id = 0

    for seat_id in tickets:
        if not min_id:
            min_id = tickets[seat_id]["seat_id"]
        if tickets[seat_id]["seat_id"] > max_id:
            max_id = tickets[seat_id]["seat_id"]
        if tickets[seat_id]["seat_id"] < min_id:
            min_id = tickets[seat_id]["seat_id"]

    return (min_id, max_id)


def solution2(tickets, ticket_bounds):
    """Find solution 2."""
    for seat_id in range(ticket_bounds[0]+1, ticket_bounds[1]+1):
        if seat_id not in tickets:
            return seat_id


def main():
    """Execute the script."""
    tickets = get_input("input.txt")
    ticket_bounds = solution1(tickets)
    print(f"Problem 1: Highest seat ID: {ticket_bounds[1]}")
    seat_id = solution2(tickets, ticket_bounds)
    print(f"Problem 2: {seat_id} is your seat ID")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
