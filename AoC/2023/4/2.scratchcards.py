#!/usr/bin/env python3
"""
Scratchcards
"""

__author__ = "J S"
__version__ = "0.1.0"
__license__ = "MIT"

import sys
from collections import defaultdict


class Scratchcards:
    def __init__(self, file_path):
        self.starting_cards = 0
        self.winnings = defaultdict(set)
        self.memo = defaultdict(int)
        self.parse_cards(file_path)

    def parse_cards(self, file_path):
        with open(file_path, "r") as file:
            for idx, line in enumerate(file):
                line = line.rstrip("\n").split(": ")[1]
                winning_nums_line, given_nums_line = line.split(" | ")
                winning_nums_line, given_nums_line = self.parse_nums(winning_nums_line), self.parse_nums(given_nums_line)
                # card 1 in idx: 1
                w = set()
                for i2 in range(1, len(winning_nums_line.intersection(given_nums_line)) + 1):
                    w.add(idx + 1 + i2)

                self.winnings[idx + 1] = w
                self.starting_cards += 1

    def parse_nums(self, num_str):
        num_str = num_str.strip().split(" ")
        # if line can have duplicate, use Counter
        nums = set(num_str)
        # cases of 2 whitespace between input: '1  6'
        if '' in nums:
            nums.remove('')
        return nums

    def traverse(self, idx, winning_cards):
        won_cards = 0
        for card in winning_cards:
            won_cards += 1
            if self.memo[card]:
                won_cards += self.memo[card]
            else:
                won_cards += self.traverse(card, self.winnings[card])
        if not self.memo[idx]:
            self.memo[idx] = won_cards
        return won_cards

    def run(self):
        # overengineered because I read the question wrong first time....
        # todo: question easily possible with one pass....

        total_cards = self.starting_cards
        for idx in range(1, self.starting_cards + 1):
            if self.memo[idx]:
                total_cards += self.memo[idx]
                continue
            won_cards = self.traverse(idx, self.winnings[idx])
            total_cards += won_cards

        print(total_cards)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    Scratchcards(sys.argv[1]).run()
