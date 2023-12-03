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

    def adj_nums(self, r, c):
        # we could fail early here..... a few times
        # refactor: a is_valid_pos function would be so much easier than re-writing these conditions....
        locations = []

        up = False
        down = False
        # look up
        if r - 1 >= 0:
            if self.grid[r - 1][c].isdigit():
                locations.append((r - 1, c))
                up = True

        if not up:
            # up left
            if r - 1 >= 0 and c - 1 >= 0:
                if self.grid[r - 1][c - 1].isdigit():
                    locations.append((r - 1, c - 1))
            # up right
            if r - 1 >= 0 and c + 1 < self.col_len:
                if self.grid[r - 1][c + 1].isdigit():
                    locations.append((r - 1, c + 1))
        # look down
        if r + 1 < self.row_len:
            if self.grid[r + 1][c].isdigit():
                locations.append((r + 1, c))
                down = True

        if not down:
            # down left
            if r + 1 < self.row_len and c - 1 >= 0:
                if self.grid[r + 1][c - 1].isdigit():
                    locations.append((r + 1, c - 1))
            # down right
            if r + 1 < self.row_len and c + 1 < self.col_len:
                if self.grid[r + 1][c + 1].isdigit():
                    locations.append((r + 1, c + 1))
        # left
        if c - 1 >= 0:
            if self.grid[r][c - 1].isdigit():
                locations.append((r, c - 1))
        # right
        if c + 1 < self.col_len:
            if self.grid[r][c + 1].isdigit():
                locations.append((r, c + 1))
        return locations

    def get_nums(self, coords):
        # expand each coord left + right
        nums = []
        for r, c in coords:
            num = self.grid[r][c]
            curr_c = c
            # left
            curr_c -= 1
            while curr_c >= 0 and self.grid[r][curr_c].isdigit():
                num = self.grid[r][curr_c] + num
                curr_c -= 1
            # right
            curr_c = c + 1
            while curr_c < self.col_len and self.grid[r][curr_c].isdigit():
                num += self.grid[r][curr_c]
                curr_c += 1
            nums.append(int(num))
        return nums

    def run(self):
        gear_ratio_sum = 0
        for r in range(self.row_len):
            for c in range(self.col_len):
                if self.grid[r][c] == "*":
                    coords = self.adj_nums(r, c)
                    no_of_nums = len(coords)
                    if no_of_nums != 2:
                        continue
                    nums = self.get_nums(coords)
                    # has to be 2
                    gear_ratio = nums[0] * nums[1]
                    gear_ratio_sum += gear_ratio

        print(gear_ratio_sum)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    Gear(sys.argv[1]).run()
