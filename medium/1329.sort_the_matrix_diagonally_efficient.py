class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        down = len(mat)
        right = len(mat[0])

        for x in range(right):
            for y in range(down):
                if x == 0 or y == 0:
                    tmp_y = y
                    tmp_x = x
                    new_diagonal = []
                    while tmp_y < down and tmp_x < right:
                        new_diagonal.append(mat[tmp_y][tmp_x])
                        tmp_y += 1
                        tmp_x += 1
                    new_diagonal.sort()
                    tmp_y = y
                    tmp_x = x
                    i = 0
                    while tmp_y < down and tmp_x < right:
                        mat[tmp_y][tmp_x] = new_diagonal[i]
                        i += 1
                        tmp_y += 1
                        tmp_x += 1
        return mat
