#!/usr/bin/env python3
"""
https://www.python-boilerplate.com/py3+executable
"""

__author__ = "J S"
__version__ = "0.1.0"
__license__ = "MIT"


import sys


def main(file_path):
    """ Main entry point of the app """
    total = 0
    with open(file_path, "r") as file:
        for line in file:
            left = None
            right = None
            val = ""
            l = 0
            r = len(line)-1
            # find left
            while left is None and l <= r:
                try:
                    left = int(line[l])
                    val += str(left)
                except ValueError:
                    l += 1
            # find right
            while right is None and l <= r:
                try:
                    right = int(line[r])
                    val += str(right)
                except ValueError:
                    r -= 1
            if right is None:
                val += val
            total += int(val)
    print(total)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main(sys.argv[1])
