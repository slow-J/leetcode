class TrieNode:
    def __init__(self, val):
        # not used
        self.val = val
        self.children = {}


class Trie:
    def __init__(self):
        # dummy node containing all starts as its children
        self.dummy = TrieNode("-1")

    def insert(self, string):
        """Insert to trie."""
        prev = self.dummy
        for char in string:
            if char in prev.children:
                prev = prev.children[char]
            else:
                new_node = TrieNode(char)
                prev.children[char] = new_node
                prev = new_node

    def check_length(self, string):
        """Gets the length of the prefix from trie."""
        curr_len = 0
        prev = self.dummy
        for char in string:
            if char in prev.children:
                prev = prev.children[char]
                curr_len += 1
            else:
                break
        return curr_len


class Solution:
    """
    Put all unique values in first array into a Trie.
    Query second array values against the Trie only if a new candidate is possible.

    ---
    Constraints:

    1 <= arr1.length, arr2.length <= 5 * 104
    1 <= arr1[i], arr2[i] <= 108
    """
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        longest = 0
        trie = Trie()

        seen = set()
        for number in arr1:
            if number in seen:
                continue
            seen.add(number)
            str_num = str(number)
            trie.insert(str_num)

        seen = set()
        for number in arr2:
            if number in seen:
                continue
            seen.add(number)
            str_num = str(number)
            if len(str_num) < longest:
                continue
            curr_len = trie.check_length(str_num)
            longest = max(longest, curr_len)
        return longest
