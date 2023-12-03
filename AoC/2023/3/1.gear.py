#!/usr/bin/env python3
"""
gear ;)
"""

__author__ = "J S"
__version__ = "0.1.0"
__license__ = "MIT"

import sys


class Gear:
    def __init__(self, file_path):
        self.grid = self.file_to_grid(file_path)
        self.row_len = len(self.grid)
        self.col_len = len(self.grid[0])

    def file_to_grid(self, file_path):
        grid = []
        with open(file_path, "r") as file:
            for row, line in enumerate(file):
                current_row = []
                for char in line.rstrip("\n"):
                    current_row.append(char)
                grid.append(current_row)
        return grid

    def isValid(self, r, c):
        # dont check left/right :p
        # check up
        if r - 1 >= 0:
            try:
                int(self.grid[r - 1][c])
            except ValueError:
                if self.grid[r - 1][c] != ".":
                    return True
        # up left
        if r - 1 >= 0 and c - 1 >= 0:
            try:
                int(self.grid[r - 1][c - 1])
            except ValueError:
                if self.grid[r - 1][c - 1] != ".":
                    return True
        # up right
        if c + 1 < self.col_len and r - 1 >= 0:
            try:
                int(self.grid[r - 1][c + 1])
            except ValueError:
                if self.grid[r - 1][c + 1] != ".":
                    return True
        # down left
        if c - 1 >= 0 and r + 1 < self.row_len:
            try:
                int(self.grid[r + 1][c - 1])
            except ValueError:
                if self.grid[r + 1][c - 1] != ".":
                    return True
        # check down
        if r + 1 < self.col_len:
            try:
                int(self.grid[r + 1][c])
            except ValueError:
                if self.grid[r + 1][c] != ".":
                    return True
        # down right
        if c + 1 < self.col_len and r + 1 < self.row_len:
            try:
                int(self.grid[r + 1][c + 1])
            except ValueError:
                if self.grid[r + 1][c + 1] != ".":
                    return True
        return False

    def run(self):
        part_number_sum = 0
        # print(self.grid)
        for r in range(self.row_len):
            current_no_str = ""
            valid = False
            for c in range(self.col_len):
                # print(r,c)
                try:
                    int(self.grid[r][c])
                    current_no_str += self.grid[r][c]
                    if not valid:
                        valid = self.isValid(r, c)
                except ValueError:
                    # if not valid, check if not . else valid = true :p else current_no_str = ""
                    if self.grid[r][c] != ".":
                        valid = True
                    if valid and current_no_str:
                        # print(current_no_str)
                        part_number_sum += int(current_no_str)
                    current_no_str = ""
                    if self.grid[r][c] == ".":
                        # this is fine because we will still check up left and bottom left
                        valid = False
            if valid and current_no_str:
                # print(current_no_str)
                part_number_sum += int(current_no_str)
        print(part_number_sum)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    Gear(sys.argv[1]).run()
