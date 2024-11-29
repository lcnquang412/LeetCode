import math


class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(math.floor(len(s) / 2)):
            tmp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = tmp


a = ["h", "e", "l", "l", "o"]
solution = Solution()
print(solution.reverseString(a))
