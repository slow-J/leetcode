class Solution:
    """
    Time complexity: O(N)
    26ms Beats 97.19%
    """
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True

        s1 = sentence1.split()
        s2 = sentence2.split()

        # shortest will always be s1
        if len(s2) < len(s1):
            s1, s2 = s2, s1

        # There are the 3 criteria for success.
        # We can insert the extra words either at:
        # 1. at start of s1
        # 2. in middle of s1
        # 3. at end of s1

        words_matched = 0
        for idx in range(len(s1)):
            if s1[idx] == s2[idx]:
                words_matched += 1
            else:
                # option 1/2 or return False
                nums_left = len(s1) - idx - 1
                idx2 = len(s2) - nums_left - 1
                while idx < len(s1):
                    if s1[idx] != s2[idx2]:
                        return False
                    idx += 1
                    idx2 += 1

                # if words_matched all
                if idx2 == len(s2):
                    return True
                else:
                    return False

        if words_matched == len(s1):
            # option 3 guaranteed
            return True
        return False
