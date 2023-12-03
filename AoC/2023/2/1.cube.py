#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "J S"
__version__ = "0.1.0"
__license__ = "MIT"

import sys


def main(file_path):
    sum_of_ids = 0
    with open(file_path, "r") as file:
        for idx, line in enumerate(file):
            valid = True
            top_blue = 0
            top_green = 0
            top_red = 0

            for group in line.rstrip("\n").split(": ")[1].split("; "):
                # print(group)
                for elem in group.split(", "):
                    val, col = elem.split(" ")
                    val = int(val)
                    if col[-1] == "e":
                        top_blue = max(top_blue, val)
                    elif col[-1] == "n":
                        top_green = max(top_green, val)
                    elif col[-1] == "d":
                        top_red = max(top_red, val)
                    else:
                        raise RuntimeError(elem)

                if top_blue > 14 or top_green > 13 or top_red > 12:
                    valid = False
                    break

            if valid:
                sum_of_ids += idx + 1
        print(sum_of_ids)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main(sys.argv[1])
