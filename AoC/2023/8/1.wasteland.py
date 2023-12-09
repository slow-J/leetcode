#!/usr/bin/env python3
"""
bruteforce
"""

__author__ = "J S"
__version__ = "0.1.0"
__license__ = "MIT"

import sys


class Wasteland:
    def __init__(self, file_path):
        self.instructions = None
        # val: (L, R)
        self.map = {}
        self.first = "AAA"
        self.parse_in(file_path)
        self.finish = "ZZZ"

    def parse_in(self, file_path):
        with open(file_path, "r") as file:
            for line in file:
                line = line.rstrip("\n")
                if not line:
                    continue

                if self.instructions is None:
                    self.instructions = line
                    continue
                # each node guaranteed to be 3 chars
                key, adj = line.split(" = ")
                left = adj[1:4]
                right = adj[-4:-1]
                self.map[key] = (left, right)

    def run(self):
        steps = 0
        idx = 0
        curr = self.first
        while True:
            if curr == self.finish:
                return steps
            step = self.instructions[idx]
            if step == "L":
                choice = 0
            else:
                choice = 1
            curr = self.map[curr][choice]

            steps += 1
            idx += 1
            if idx == len(self.instructions):
                idx = 0


if __name__ == "__main__":
    """ This is executed when run from the command line """
    steps = Wasteland(sys.argv[1]).run()
    print(steps)
