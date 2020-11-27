class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        next_row = 0
        down = True
        strings_list = [""] * numRows

        for char in s:
            if down:
                strings_list[next_row] += char
                if next_row < numRows:
                    next_row += 1
                if next_row == numRows - 1:
                    down = False
            else:
                strings_list[next_row] += char
                if next_row > 0:
                    next_row -= 1
                if next_row == 0:
                    down = True

        return (''.join(strings_list))
