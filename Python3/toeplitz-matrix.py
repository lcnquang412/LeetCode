class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        def goDiagonal(_row, _col) -> bool:
            value = matrix[_row][_col]
            count = min(row - _row, col - _col)
            for j in range(count):
                if matrix[_row][_col] != value:
                    return False
                _row += 1
                _col += 1
            return True

        for i in range(0, col):
            if not goDiagonal(0, i):
                return False

        for i in range(1, row):
            if not goDiagonal(i, 0):
                return False

        return True


a = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
# a = [[1, 2], [2, 2]]
solution = Solution()
print(solution.isToeplitzMatrix(a))
