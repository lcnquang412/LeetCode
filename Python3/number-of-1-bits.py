class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n != 0:
            result += n & 1
            n = n >> 1
        return result


a = 2147483645
# a = 10
solution = Solution()
print(solution.hammingWeight(a))
