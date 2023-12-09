#!/usr/bin/env python3
"""
:D
"""

__author__ = "J S"
__version__ = "0.1.0"
__license__ = "MIT"

import sys
from collections import Counter

card_val = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


class Node:
    def __init__(self, hand, bid, next1=None):
        self.hand = hand
        self.hand_c = Counter(hand)
        self.jokers = hand.count('J')
        # think this is the way
        # del self.hand_c['J']
        self.hand_c['J'] = 0

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

    def compare_from_start(self, node1, node2):
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
    def is_left_bigger(self, node1, node2):
        hand1_c = node1.hand_c.most_common(2)
        hand2_c = node2.hand_c.most_common(2)
        joker1 = node1.jokers
        joker2 = node2.jokers
        # print(hand1_c, hand1_c[0][1])
        # print(hand2_c)
        if hand1_c[0][1] + joker1 > hand2_c[0][1] + joker2:
            return True
        elif hand1_c[0][1] + joker1 < hand2_c[0][1] + joker2:
            return False
        elif hand1_c[0][1] + joker1 == hand2_c[0][1] + joker2 and (
            (hand1_c[0][1] + joker1 == 1) or (hand1_c[0][1] + joker1 == 4) or (hand1_c[0][1] + joker1 == 5)):
            # print(hand1_c, joker1, " ", hand2_c, joker2)
            return self.compare_from_start(node1, node2)
        # ==
        # check full house
        # if both 3 (they are the same)
        print(hand1_c[0][1] + joker1, hand2_c[0][1] + joker2)
        if hand1_c[0][1] + joker1 >= 3 and hand2_c[0][1] + joker2 >= 3:
            print('!!!!!!!!!!!!!!!!')
            if hand1_c[0][1] == 4:
                raise Exception("e")
            if hand2_c[0][1] == 4:
                raise Exception("e")
            jokers_left1 = joker1 - (3 - hand1_c[0][1])
            jokers_left2 = joker2 - (3 - hand2_c[0][1])
            # print(node1.hand, jokers_left1, node2.hand)
            print('?', node1.hand_c, hand1_c, joker1, jokers_left1, hand2_c, joker2, jokers_left2)
            if hand1_c[1][1] + jokers_left1 == 2 and hand2_c[1][1] + jokers_left2 < 2:
                print('t', node1.hand_c, hand1_c, joker1, jokers_left1, hand2_c, joker2, jokers_left2)
                return True
            elif (jokers_left2 == 2 or hand2_c[1][1] + jokers_left2 == 2) and hand1_c[1][1] + jokers_left1 < 2:
                print('f', node1.hand_c, hand1_c, joker1, jokers_left1, node2.hand_c,hand2_c, joker2, jokers_left2)
                return False
            # return self.compare_from_start(node1, node2)

        # 2 pairs can't beat this, draw
        if hand1_c[0][1] + joker1 >= 3 or hand2_c[0][1] + joker2  >= 3:
            return self.compare_from_start(node1, node2)

        # check 2 pairs
        if hand1_c[0][1] + joker1 >= 2 and hand2_c[0][1] + joker2 >= 2:
            # if hand1_c[0][1] == 3:
            #     raise Exception("e")
            # if hand2_c[0][1] == 3:
            #     raise Exception("e")
            jokers_left1 = joker1
            jokers_left2 = joker2
            if hand1_c[0][1] < 2:
                jokers_left1 = joker1 - (2 - hand1_c[0][1])

            if hand2_c[0][1] < 2:
                jokers_left2 = joker2 - (2 - hand2_c[0][1])
            if hand1_c[1][1] + jokers_left1 == 2 and hand2_c[1][1] + jokers_left2 < 2:
                print('t', node1.hand_c, hand1_c, joker1, jokers_left1, hand2_c, joker2, jokers_left2)
                return True
            elif hand2_c[1][1] + jokers_left2 == 2 and hand1_c[1][1] + jokers_left1 < 2:
                print('f', node1.hand_c, hand1_c, joker1, jokers_left1, node2.hand_c,hand2_c, joker2, jokers_left2)
                return False

        return self.compare_from_start(node1, node2)


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
            print(rank, curr.hand, curr.bid, current_winnings)
            total_winnings += current_winnings
        print(total_winnings)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    Camel(sys.argv[1]).run()
