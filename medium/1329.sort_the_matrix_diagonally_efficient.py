class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        numrows = len(mat)
        numcols = len(mat[0])

        for x in range(numcols):
            for y in range(numrows):
                if x == 0 or y == 0:
                    tmp_y = y
                    tmp_x = x

                    # Get the diagonal.
                    new_diagonal = []
                    while tmp_y < numrows and tmp_x < numcols:
                        new_diagonal.append(mat[tmp_y][tmp_x])
                        tmp_y += 1
                        tmp_x += 1

                    # Sort and replace.
                    new_diagonal.sort()
                    tmp_y = y
                    tmp_x = x
                    i = 0
                    while tmp_y < numrows and tmp_x < numcols:
                        mat[tmp_y][tmp_x] = new_diagonal[i]
                        i += 1
                        tmp_y += 1
                        tmp_x += 1
        return mat
