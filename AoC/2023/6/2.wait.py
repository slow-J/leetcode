#!/usr/bin/env python3
"""
easy compared to yesterday....
"""

__author__ = "J S"
__version__ = "0.1.0"
__license__ = "MIT"

import sys


class Wait:
    def __init__(self, file_path):
        self.dist = 0
        self.time = 0
        self.parse_in(file_path)

    def parse_in(self, file_path):
        with open(file_path, "r") as file:
            time = ""
            dist = ""
            for line in file:
                line = line.rstrip("\n")
                funct, vals = line.split(":")
                vals_parsed = vals.split()
                if funct == "Time":
                    for t in vals_parsed:
                        time += t
                elif funct == "Distance":
                    for d in vals_parsed:
                        dist += d
            self.dist = int(dist)
            self.time = int(time)

    def run(self):
        ways_to_win = 0
        found = False
        for i2 in range(1, self.time):
            # skip 0 and max dist
            speed = i2
            time_left = self.time - i2
            travelled = time_left * speed
            # todo: could use some heuristic to skip ahead
            if self.dist < travelled:
                ways_to_win += 1
                # print(travelled)
                found = True
            elif found:
                break

        print(ways_to_win)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    Wait(sys.argv[1]).run()
