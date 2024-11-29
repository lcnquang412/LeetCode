class Solution:
    def reverse(self, x: int) -> int:
        result = int(f'{abs(x)}'[::-1]) * (-1 if x < 0 else 1)
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0
        return result


a = 123
a = -123
# a = 120
a = 1534236469
solution = Solution()
print(solution.reverse(a))
