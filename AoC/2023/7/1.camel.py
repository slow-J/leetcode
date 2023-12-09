#!/usr/bin/env python3
"""
easy compared to yesterday....
"""

__author__ = "J S"
__version__ = "0.1.0"
__license__ = "MIT"

import sys
from collections import Counter

card_val = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class Node:
    def __init__(self, hand, bid, next1=None):
        self.hand = hand
        self.hand_c = Counter(hand)
        self.bid = bid
        self.next = next1


class Camel:
    def __init__(self, file_path):
        self.hands = []
        self.bids = []
        self.parse_in(file_path)
        # dummy pointer
        # in order of largest -> smallest
        self.ll = Node("-1", -1)

    def parse_in(self, file_path):
        with open(file_path, "r") as file:
            for line in file:
                line = line.rstrip("\n")
                hand, bid = line.split(" ")
                self.hands.append(hand)
                self.bids.append(int(bid))

    def is_left_bigger(self, node1, node2):
        hand1_c = node1.hand_c.most_common(2)
        hand2_c = node2.hand_c.most_common(2)
        # print(hand1_c, hand1_c[0][1])
        # print(hand2_c)
        if hand1_c[0][1] > hand2_c[0][1]:
            return True
        elif hand1_c[0][1] < hand2_c[0][1]:
            return False
        # ==
        # check full house
        # if both 3 (they are the same)
        if hand1_c[0][1] == 3:
            if hand1_c[1][1] == 2 and hand2_c[1][1] != 2:
                return True
            elif hand2_c[1][1] == 2 and hand1_c[1][1] != 2:
                # print('f')
                return False
        # check 2 pairs
        if hand1_c[0][1] == 2:
            if hand1_c[1][1] == 2 and hand2_c[1][1] != 2:
                return True
            elif hand2_c[1][1] == 2 and hand1_c[1][1] != 2:
                # print('f')
                return False
        # If two hands have the same type, a second ordering rule takes effect.
        # Start by comparing the first card in each hand. If these cards are different,
        # the hand with the stronger first card is considered stronger. If the first card in each hand have the same
        # label, however, then move on to considering the second card in each hand. If they differ, the hand with
        # the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.
        for char1, char2 in zip(node1.hand, node2.hand):
            val1, val2 = card_val[char1], card_val[char2]
            if val1 > val2:
                return True
            elif val1 < val2:
                return False
        # shouldn't happen
        raise Exception("e")

    def insert_to_ll(self, hand, bid):
        new_node = Node(hand, bid)

        prev = None
        curr = self.ll
        while curr.next:
            prev = curr
            curr = curr.next
            if self.is_left_bigger(new_node, curr):
                new_node.next = curr
                prev.next = new_node
                return
        # if last
        curr.next = new_node

    def run(self):
        for idx in range(len(self.hands)):
            self.insert_to_ll(self.hands[idx], self.bids[idx])
        total_winnings = 0
        rank = len(self.hands) + 1
        # go through ll
        curr = self.ll
        while curr.next:
            rank -= 1
            curr = curr.next
            current_winnings = rank * curr.bid
            # print(rank, curr.hand, curr.bid, current_winnings)
            total_winnings += current_winnings
        print(total_winnings)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    Camel(sys.argv[1]).run()
