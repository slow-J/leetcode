class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numerals_conversion = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        v_x = {"V", "X"}
        l_c = {"L", "C"}
        d_m = {"D", "M"}
        skip_next = False
        str_len = len(s)
        running_total = 0
        for i, char in enumerate(s):
            if not skip_next:
                if i < str_len - 1:
                    if char == "I" and s[i + 1] in v_x:
                        skip_next = True
                        if s[i + 1] == "V":
                            running_total += 4
                        else:
                            running_total += 9
                    elif char == "X" and s[i + 1] in l_c:
                        skip_next = True
                        if s[i + 1] == "L":
                            running_total += 40
                        else:
                            running_total += 90
                    elif char == "C" and s[i + 1] in d_m:
                        skip_next = True
                        if s[i + 1] == "D":
                            running_total += 400
                        else:
                            running_total += 900
                    else:
                        running_total += numerals_conversion[char]
                else:
                    running_total += numerals_conversion[char]
            else:
                skip_next = False
        return running_total
