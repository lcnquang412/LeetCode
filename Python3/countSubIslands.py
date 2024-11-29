a = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
b = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]


class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        row = len(grid2)
        col = len(grid2[0])
        countSubIsland = 0

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid2[r][c] == 0:
                return True
            isSubIsland = grid1[r][c] == 1
            grid2[r][c] = 0
            isSubIsland &= dfs(r - 1, c)
            isSubIsland &= dfs(r + 1, c)
            isSubIsland &= dfs(r, c - 1)
            isSubIsland &= dfs(r, c + 1)
            return isSubIsland

        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1 and dfs(i, j):
                    countSubIsland += 1

        return countSubIsland


solution = Solution()
print(solution.countSubIslands(a, b))
