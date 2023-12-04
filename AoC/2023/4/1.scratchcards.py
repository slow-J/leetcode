#!/usr/bin/env python3
"""
Scratchcards
"""

__author__ = "J S"
__version__ = "0.1.0"
__license__ = "MIT"

import sys


class Scratchcards:
    def parse_nums(self, num_str):
        num_str = num_str.strip().split(" ")
        # if line can have duplicate, use Counter
        nums = set(num_str)
        # cases of 2 whitespace between input: '1  6'
        if '' in nums:
            nums.remove('')
        return nums

    def run(self, file_path):
        total_points = 0

        with open(file_path, "r") as file:
            for row, line in enumerate(file):
                line_points = 0
                line = line.rstrip("\n").split(": ")[1]
                winning_nums, line_nums = line.split(" | ")
                winning_nums, line_nums = self.parse_nums(winning_nums), self.parse_nums(line_nums)
                winning = len(winning_nums.intersection(line_nums))
                for _ in range(winning):
                    if not line_points:
                        line_points += 1
                    else:
                        line_points *= 2
                total_points += line_points

        print(total_points)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    Scratchcards().run(sys.argv[1])
