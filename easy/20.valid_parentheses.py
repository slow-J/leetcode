from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket = {"{", "(", "["}
        close_bracket = {"}", ")", "]"}

        last_open_bracket = deque()
        for brac in s:
            if brac in open_bracket:
                # inverse of bracket so } instead of {
                if brac == "(":
                    last_open_bracket.append(")")
                if brac == "[":
                    last_open_bracket.append("]")
                if brac == "{":
                    last_open_bracket.append("}")
            else:
                if not last_open_bracket:
                    return False
                elif brac != last_open_bracket.pop():
                    return False
        if last_open_bracket:
            return False
        return True
