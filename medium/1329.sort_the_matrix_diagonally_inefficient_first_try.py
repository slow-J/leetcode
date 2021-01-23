class Solution(object):
    def extract_diagonals(self, right, down, mat):
        diagonals = []
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
                    diagonals.append(new_diagonal)
        return diagonals

    def place_diagonals(self, right, down, diagonals):
        remade_matrix = [[0] * right for _ in range(down)]
        diagonal_index_y = 0
        diagonal_index_x = 0
        for x in range(right):
            for y in range(down):
                if x == 0 or y == 0:
                    tmp_y = y
                    tmp_x = x
                    i = 0
                    while tmp_y < down and tmp_x < right:
                        remade_matrix[tmp_y][tmp_x] = diagonals[diagonal_index_y][diagonal_index_x]
                        tmp_y += 1
                        tmp_x += 1
                        i += 1
                        diagonal_index_x += 1
                    diagonal_index_y += 1
                    diagonal_index_x = 0
        return remade_matrix

    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        down = len(mat)
        right = len(mat[0])

        diagonals = self.extract_diagonals(right, down, mat)
        sorted_diagonals = [sorted(diagonal) for diagonal in diagonals]

        return self.place_diagonals(right, down, sorted_diagonals)
