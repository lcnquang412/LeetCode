import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        resultLog = math.log(n, 4)
        return math.ceil(resultLog) - resultLog <= 0.00000000001


a = 16
# a = 243
# a = 1594322
solution = Solution()
print(solution.isPowerOfFour(a))
