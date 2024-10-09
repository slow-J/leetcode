class Solution:
    """Very similar to the daily question from yesterday. Greedy algorithm.
    Runtime: O(N) 27ms, beats 93.79%
    """

    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        total_missed = 0
        for char in s:
            if char == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    total_missed += 1
            else:
                stack.append(char)
        # Result is the count of all closed brackets with no corresponding opening, they each need a '('.
        # + count of all remaining unclosed brackets, they each need a ')'.
        return total_missed + len(stack)
