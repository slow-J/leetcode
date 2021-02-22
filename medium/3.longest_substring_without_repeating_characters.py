class Solution2:
    """Sliding window. Very quick O(N) and good on memory.
    Runtime: 52 ms, faster than 92.84%
    Memory Usage: 14.2 MB, less than 94.27%"""

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        biggest = 1
        left_pointer = 0
        right_pointer = 1
        current = set(s[0])
        len_str = len(s)
        while right_pointer < len_str:
            if s[right_pointer] not in current:
                current.add(s[right_pointer])
                right_pointer += 1
            else:
                if right_pointer - left_pointer > biggest:
                    biggest = right_pointer - left_pointer

                current.remove(s[left_pointer])
                left_pointer += 1
        if right_pointer - left_pointer > biggest:
            biggest = right_pointer - left_pointer
        return biggest
