class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            subResult = [1]
            for j in range(1, i):
                subResult.append(result[i - 1][j - 1] + result[i - 1][j])
            subResult.append(1)
            result.append(subResult)
        return result


solution = Solution()
print(solution.generate(30))
