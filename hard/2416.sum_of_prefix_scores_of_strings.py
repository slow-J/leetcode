class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0


class Solution:
    """Question is worded funny. Best explained by an example:
    "abc" has 3 prefixes: "a", "ab", and "abc"
    There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
    The total is answer[0] = 2 + 2 + 1 = 5.

    Build a trie from the words and everytime that a node is traversed during building, increment the value.
    
    Runtime:1691ms
    Beats 87.08%
    
    Time complexity: O(N∗M)
    """
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Root of the trie with a useless head.
        dummy = TrieNode()
        prefix_vals = []
        for word in words:
            node = dummy
            for char in word:
                if char in node.children:
                    node = node.children[char]
                else:
                    new_node = TrieNode()
                    node.children[char] = new_node
                    node = new_node
                node.val += 1

        for word in words:
            node = dummy
            val = 0
            for char in word:
                node = node.children[char]
                val += node.val
            prefix_vals.append(val)
        return prefix_vals
