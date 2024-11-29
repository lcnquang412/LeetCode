import math
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None:
            return True
        s = re.sub(r"[^a-z0-9]", "", s.lower())
        length = len(s)
        if length <= 1:
            return True
        for i in range(math.floor(length / 2)):
            if s[i] != s[length - 1 - i]:
                return False
        return True


a = "A man, a plan, a canal: Panama"
a = "race a car"
a = " "
a = "0P"
solution = Solution()
print(solution.isPalindrome(a))
