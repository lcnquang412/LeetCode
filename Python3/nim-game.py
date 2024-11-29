class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


a = 5
solution = Solution()
print(solution.canWinNim(a))
# 1 2 3 => W
# 4 => L
# 5 6 7 => W
# 8 -> 5 6 7 => L
# 9 -> 6 7 >8< => W
# 10 -> 7 >8< 9 => W
# 11 -> >8< 9 10 => W
# 12 -> 9 10 11 => L
