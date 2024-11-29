class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        result = []
        subResult = []
        cCount = 0
        for i in range(m):
            for j in range(n):
                cCount += 1
                subResult.append(mat[i][j])
                if cCount == c:
                    result.append(subResult)
                    subResult = []
                    cCount = 0
        return result


a = [[1, 2], [3, 4]]
b = 1
c = 4
b = 2
c = 4
solution = Solution()
print(solution.matrixReshape(a, b, c))
