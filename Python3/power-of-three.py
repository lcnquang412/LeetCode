import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        resultLog = math.log(n, 3)
        return math.ceil(resultLog) - resultLog <= 0.00000000001


a = 27
# a = 243
# a = 1594322
solution = Solution()
print(solution.isPowerOfThree(a))
