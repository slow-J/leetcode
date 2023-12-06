#!/usr/bin/env python3
"""
TODO: cleanup
"""

__author__ = "J S"
__version__ = "0.1.0"
__license__ = "MIT"

import sys
from enum import Enum


class ParseMode(Enum):
    NONE = 0
    SEED = 1
    S2S = 2
    S2F = 3
    F2W = 4
    W2L = 5
    L2T = 6
    T2H = 7
    H2L = 8


line_names = {
    "seeds": ParseMode.SEED,
    "seed-to-soil": ParseMode.S2S,
    "soil-to-fertilizer": ParseMode.S2F,
    "fertilizer-to-water": ParseMode.F2W,
    "water-to-light": ParseMode.W2L,
    "light-to-temperature": ParseMode.L2T,
    "temperature-to-humidity": ParseMode.T2H,
    "humidity-to-location": ParseMode.H2L,
}

s2s = {}
s2f = {}
f2w = {}
w2l = {}
l2t = {}
t2h = {}
h2l = {}

mode2dict = {
    ParseMode.S2S: s2s,
    ParseMode.S2F: s2f,
    ParseMode.F2W: f2w,
    ParseMode.W2L: w2l,
    ParseMode.L2T: l2t,
    ParseMode.T2H: t2h,
    ParseMode.H2L: h2l,
}


class Seeds:
    def __init__(self, file_path):
        self.seeds = None
        self.process_almanac(file_path)

    def insert_to_dict(self, mode, src, dest, range1):
        mode2dict[mode][src] = (dest, range1)

    def process_almanac(self, file_path):
        with open(file_path, "r") as file:
            curr_parse_mode = ParseMode.NONE
            for line_idx, line in enumerate(file):
                # empty line = reset parse mode
                if line == "\n":
                    curr_parse_mode = ParseMode.NONE
                    continue
                # if no current mode
                if curr_parse_mode == ParseMode.NONE:
                    line = line.rstrip("\n")
                    if line and line[-1] == ":":
                        mode_name, rest_of_line = line.rstrip("\n").split(" map:")
                    else:
                        mode_name, rest_of_line = line.rstrip("\n").split(": ")
                    curr_parse_mode = line_names[mode_name]
                    # seeds parsed instantly
                    if curr_parse_mode == ParseMode.SEED:
                        self.seeds = rest_of_line.split(" ")
                else:
                    dest, src, range1 = line.rstrip("\n").split(" ")
                    # dest, src, range_len = int(dest), int(src), int(range_len)
                    range1 = int(range1)
                    self.insert_to_dict(curr_parse_mode, src, dest, range1)

    @staticmethod
    def search(dict1, k):
        # dict1.get(k, k)

        int_k = int(k)
        # src, dest, range
        closest = None
        close_val = float("inf")
        for key in dict1:
            # print(int_k - int(dict1[key][0]))
            if int_k - int(key) >= 0:
                if int_k - int(key) < close_val:
                    close_val = int_k - int(key)
                    closest = key
        if not closest:
            return k
        # print(k, "closest", dict1[closest])
        src = closest
        dest, range1 = dict1[closest]

        offset = int(dest) - int(src)
        if int_k <= int(src) + range1:
            return str(int_k + offset)
        return k

    def s2l(self, seed):
        # Any source numbers that aren't mapped correspond to the same destination number.
        # So, seed number 10 corresponds to soil number 10.
        soil = self.search(s2s, seed)
        fertilizer = self.search(s2f, soil)
        water = self.search(f2w, fertilizer)
        light = self.search(w2l, water)
        temperature = self.search(l2t, light)
        humidity = self.search(t2h, temperature)
        location = self.search(h2l, humidity)
        return location

    def run(self):
        # print(w2l)
        lowest_l = float("inf")
        for seed in self.seeds:
            # print(int(self.s2l(seed)))
            lowest_l = min(lowest_l, int(self.s2l(seed)))
        print(lowest_l)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    Seeds(sys.argv[1]).run()
