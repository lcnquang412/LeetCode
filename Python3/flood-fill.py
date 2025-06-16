class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        stack = []
        originalColor = image[sr][sc]
        rowMax = len(image)
        colMax = len(image[0])
        stack.append([sr, sc])

        def appendStack(_row: int, _col: int):
            if (0 <= _row < rowMax
                    and 0 <= _col < colMax
                    and image[_row][_col] == originalColor
                    and image[_row][_col] != color):
                stack.append([_row, _col])

        while len(stack) > 0:
            coordinate = stack.pop()
            row = coordinate[0]
            col = coordinate[1]
            image[row][col] = color

            appendStack(row + 1, col)
            appendStack(row - 1, col)
            appendStack(row, col + 1)
            appendStack(row, col - 1)
        return image


# a = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# b = 1
# c = 1
# d = 2

a = [[0, 0, 0], [0, 0, 0]]
b = 0
c = 0
d = 0
solution = Solution()
print(solution.floodFill(a, b, c, d))
