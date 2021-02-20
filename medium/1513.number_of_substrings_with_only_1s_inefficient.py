class Solution:
    def __init__(self):
        self.max_num = 10 ** 9 + 7
        self.dp = {1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21}
        # Needed only with bottom up.
        # self.biggest = 6

    """Top down implementation for substrings_in_string_of_1s.
    Runtime: 92 ms, faster than 26%
    Memory Usage: 14.7 MB - 70%"""

    def substrings_in_string_of_1s(self, length):
        """We find amount of total substrings in a string of just 1's of length x."""
        original_length = length
        substring_total = 0
        while length > 0:
            if length in self.dp:
                substring_total += self.dp[length]
                break
            substring_total += length
            length -= 1
        if original_length not in self.dp:
            self.dp[original_length] = substring_total
        return substring_total

    """Bottom up implementation for substrings_in_string_of_1s.
    Runtime: 100 ms, faster than 18.43%
    Memory Usage: 30.7 MB, less than 5.37%"""

    def substrings_in_string_of_1s(self, length):
        """We find amount of total substrings in a string of just 1's of length x."""
        original_length = length
        start = min(self.biggest, length)
        substring_total = self.dp[start]
        start = start + 1
        while start <= length:
            substring_total += start
            self.dp[start] = substring_total
            start += 1
        self.biggest = original_length
        return substring_total

    def numSub(self, s: str) -> int:
        nums = 0
        str_len = len(s)
        i = 0
        while i < str_len:
            if s[i] == "1":
                i2 = i + 1
                while i2 < str_len:
                    if s[i2] == "1":
                        i2 += 1
                    else:
                        break
                length_of_1s = i2 - i
                nums += self.substrings_in_string_of_1s(length_of_1s)
                i = i2
            else:
                i += 1
        return nums % self.max_num
