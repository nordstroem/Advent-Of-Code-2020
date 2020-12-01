#!/bin/python3

import argparse
import sys
from days import *  # pylint: disable=unused-wildcard-import


def main(argv):
    parser = argparse.ArgumentParser(description="run advent of code")
    parser.add_argument("day", type=int, help='day')
    parser.add_argument("part", type=int, help='part')
    args = parser.parse_args(argv)
    part = getattr(sys.modules["days.day{}".format(args.day)], "part{}".format(args.part))
    part()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
