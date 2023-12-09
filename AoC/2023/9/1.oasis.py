#!/usr/bin/env python3
"""
a
"""

__author__ = "J S"
__version__ = "0.1.0"
__license__ = "MIT"

import sys


class Oasis:
    def __init__(self, file_path):
        # list of list
        self.lines = []
        self.parse_in(file_path)

    def parse_in(self, file_path):
        with open(file_path, "r") as file:
            for line in file:
                line = line.rstrip("\n")

                line_vals = line.split(" ")
                line_vals = [int(val) for val in line_vals]
                self.lines.append(line_vals)

    def run(self):
        total_next = 0
        for line in self.lines:
            next_lines = []
            curr_line = line
            found = False
            while not found:
                next_line = []
                zeros = 0
                prev = curr_line[0]
                for val in curr_line[1:]:
                    diff = val - prev
                    prev = val
                    next_line.append(diff)
                    if diff == 0:
                        zeros += 1
                next_lines.append(next_line)
                curr_line = next_line
                if zeros == len(next_line):
                    found = True
            # print(line, next_lines)

            # iterate through next_lines backwards
            idx = len(next_lines) - 1
            prev = next_lines[idx][-1]
            idx -= 1
            while idx >= 0:
                curr = next_lines[idx][-1]
                prev = curr + prev
                idx -= 1
            # print(prev)
            extrapolated_val = line[-1] + prev
            total_next += extrapolated_val
        print(total_next)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    Oasis(sys.argv[1]).run()
