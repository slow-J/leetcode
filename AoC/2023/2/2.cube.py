#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "J S"
__version__ = "0.1.0"
__license__ = "MIT"

import sys


def main(file_path):
    total_power = 0
    with open(file_path, "r") as file:
        for line in file:
            top_blue = 0
            top_green = 0
            top_red = 0

            for group in line.rstrip("\n").split(": ")[1].split("; "):
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

            game_power = top_blue * top_green * top_red
            total_power += game_power
        print(total_power)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main(sys.argv[1])
