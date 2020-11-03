class Solution:
    # def isPalindrome(self, x: int) -> bool:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
