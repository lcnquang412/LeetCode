class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        result = [1] * 3
        for i in range(3, rowIndex + 2):
            tmp = result
            result = [1] * i
            for j in range(1, i - 1):
                result[j] = tmp[j] + tmp[j - 1]
        return result


solution = Solution()
print(solution.getRow(5))
