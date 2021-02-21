class Solution:
    """Splitting string into lists of just 1's and using maths to calculate substrings.
    Runtime: 36 ms, faster than 98.87%
    Memory Usage: 15.1 MB - 36.44%"""

    def __init__(self):
        self.max_num = 10 ** 9 + 7

    def substrings_in_string_of_1s(self, length):
        """We find amount of total substrings in a string of just 1's of length x."""
        return ((length + 1) * length) // 2

    def numSub(self, s: str) -> int:
        ones_substrings = s.split("0")
        num_of_substrings = 0
        length = 0
        for ones in ones_substrings:
            length = len(ones)
            if length > 0:
                num_of_substrings += self.substrings_in_string_of_1s(length)
        if num_of_substrings < self.max_num:
            return num_of_substrings
        return num_of_substrings % self.max_num
