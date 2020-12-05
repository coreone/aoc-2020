#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys

import requests


def parse_arguments():
    """Parse command-line arguments using argparse."""
    parser = argparse.ArgumentParser(description="Input getter")
    parser.add_argument("-d", "--day", help="The day to retrieve", required=True)

    return parser.parse_args()


def get_input(day):
    """Retrieve the input for the AoC day."""
    url = f"https://adventofcode.com/2020/day/{day}/input"
    pwd = os.path.realpath(os.path.dirname(__file__))

    with open(os.path.join(pwd, "session.txt"), "r") as filep:
        cookie = filep.readline().strip()

    sess = requests.Session()
    jar = requests.cookies.RequestsCookieJar()
    jar.set("session", cookie)
    res = sess.get(url, cookies=jar)

    daydir = os.path.join(pwd, f"day{day}")
    if not os.path.isdir(daydir):
        os.mkdir(daydir, 0o755)

    with open(os.path.join(daydir, f"day{day}.txt"), "w") as filep:
        filep.write(res.text.strip())


def main():
    """Execute the script."""
    args = parse_arguments()

    get_input(args.day)

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
