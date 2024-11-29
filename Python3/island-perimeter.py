class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i - 1 < 0 or grid[i - 1][j] == 0:
                        result += 1
                    if i + 1 == len(grid) or grid[i + 1][j] == 0:
                        result += 1
                    if j - 1 < 0 or grid[i][j - 1] == 0:
                        result += 1
                    if j + 1 == len(grid[i]) or grid[i][j + 1] == 0:
                        result += 1
        return result


a = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
a = [[1]]
a = [[1, 0]]
solution = Solution()
print(solution.islandPerimeter(a))
