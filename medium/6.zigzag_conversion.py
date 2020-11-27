class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        next_col = 0
        down = True
        list_2d = [list() for elem in range(numRows)]

        for char in s:
            if down:
                list_2d[next_col].append(char)
                if next_col < numRows:
                    next_col += 1
                if next_col == numRows - 1:
                    down = False
            else:
                list_2d[next_col].append(char)
                if next_col > 0:
                    next_col -= 1
                if next_col == 0:
                    down = True

        return (''.join(item for inner_list in list_2d for item in inner_list))
