import re


class Solution(object):
    def isPalindrome(self, s):
        """
        Regex needed to remove non-alphanumeric characters.

        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        s = s.lower().replace(' ', '')
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        return s == s[::-1]
