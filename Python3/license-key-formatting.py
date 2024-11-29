import math


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        length = len(s)
        firstGroupLength = k if length % k == 0 else length % k
        result = s[0:firstGroupLength]
        for i in range(math.ceil(length / k) - 1):
            left = firstGroupLength + i * k
            right = firstGroupLength + (i + 1) * k
            result += f'-{s[left:right]}'
        return result


a = "5F3Z-2e-9-w"
b = 4
# a = "2-5g-3-J"
# b = 2
# a = "2-4A0r7-4k"
# b = 3
solution = Solution()
print(solution.licenseKeyFormatting(a, b))
