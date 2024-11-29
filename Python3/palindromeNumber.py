import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if 0 <= x <= 9:
            return True
        s = f'{x}'
        length = len(s)
        for left in range(0, math.floor(length / 2)):
            if s[left] != s[length - left - 1]:
                return False
        return True


solution = Solution()
print(solution.isPalindrome(1235321))
