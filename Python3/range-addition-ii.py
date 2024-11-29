class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        minRow = m
        minColumn = n
        for op in ops:
            minRow = min(minRow, op[0])
            minColumn = min(minColumn, op[1])
        return minRow * minColumn


a = 3
b = 3
c = [[2, 2], [3, 3]]
c = [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]
c = []
solution = Solution()
print(solution.maxCount(a, b, c))
