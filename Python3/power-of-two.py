class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        i = 1
        tmp = 2
        while tmp <= n:
            if tmp == n:
                return True
            i += 1
            tmp = 2 ** i
        return False


a = 18
solution = Solution()
print(solution.isPowerOfTwo(a))
