#!/usr/bin/env python3
"""
This is quick and dirty...
backtracking trie, could probably optimize this a lot...
"""

__author__ = "J S"
__version__ = "0.1.0"
__license__ = "MIT"


import sys


class TrieNode:
    def __init__(self, val):
        self.val = val
        # val: node
        self.children = {}
        # 0 not valid
        self.finished = 0


valid_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def generate_trie(backwards=False):
    root = TrieNode("dummy")
    for idx, num in enumerate(valid_nums):
        tmp = root

        for char in _reverse(num, backwards):
            if char in tmp.children:
                tmp = tmp.children[char]
            else:
                new_node = TrieNode(char)
                tmp.children[char] = new_node
                tmp = new_node
        tmp.finished = idx + 1
    return root


def _reverse(num, backwards):
    if not backwards:
        return num
    else:
        return num[::-1]


def main(file_path):
    f_trie_root = generate_trie()
    b_trie_root = generate_trie(backwards=True)

    total = 0
    with open(file_path, "r") as file:
        for line in file:
            left = None
            right = None
            val = ""
            l = 0
            r = len(line)-1

            # find left
            trie_root = f_trie_root
            current_trie_node = trie_root

            # backtrack
            start_traversal = l
            while left is None and l <= r:
                try:
                    left = int(line[l])
                    val += str(left)
                except ValueError:
                    curr_l = line[l]
                    if curr_l in current_trie_node.children:
                        if current_trie_node.children[curr_l].finished:
                            left = current_trie_node.children[curr_l].finished
                            val += str(left)
                        else:
                            current_trie_node = current_trie_node.children[curr_l]
                        l += 1
                    else:
                        current_trie_node = trie_root
                        l = start_traversal + 1
                        start_traversal = l

            # backtrack
            start_traversal = r
            trie_root = b_trie_root
            current_trie_node = trie_root

            # find right
            while right is None and 0 <= r:
                try:
                    right = int(line[r])
                    val += str(right)
                except ValueError:
                    curr_r = line[r]
                    if curr_r in current_trie_node.children:
                        if current_trie_node.children[curr_r].finished:
                            right = current_trie_node.children[curr_r].finished
                            val += str(right)
                        else:
                            current_trie_node = current_trie_node.children[curr_r]
                        r -= 1
                    else:
                        current_trie_node = trie_root
                        r = start_traversal - 1
                        start_traversal = r
            # print(val, line)
            total += int(val)
    print(total)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main(sys.argv[1])
