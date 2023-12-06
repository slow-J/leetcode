#!/usr/bin/env python3
"""
foo
"""

__author__ = "J S"
__version__ = "0.1.0"
__license__ = "MIT"

import sys


class Wait:
    def __init__(self, file_path):
        self.dists = []
        self.times = []
        self.parse_in(file_path)

    def parse_in(self, file_path):
        with open(file_path, "r") as file:
            for line in file:
                line = line.rstrip("\n")
                funct, vals = line.split(":")
                vals_parsed = vals.split()
                # print(vals_parsed)
                if funct == "Time":
                    for t in vals_parsed:
                        self.times.append(int(t))
                elif funct == "Distance":
                    for d in vals_parsed:
                        self.dists.append(int(d))

    def run(self):
        total_ways = 1
        for i in range(len(self.times)):
            # game i
            dist = self.dists[i]
            time = self.times[i]
            ways_to_win = 0
            found = False
            for i2 in range(1, time):
                # skip 0 and max dist
                speed = i2
                time_left = time - i2
                travelled = time_left * speed
                # todo: could use some heuristic to skip ahead
                if dist < travelled:
                    ways_to_win += 1
                    # print(travelled)
                    found = True
                elif found:
                    break
            total_ways *= ways_to_win

        print(total_ways)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    Wait(sys.argv[1]).run()
