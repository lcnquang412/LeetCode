class Solution:

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        s = '#' + '#'.join(s) + '#'
        print(s)


a = 'babad'
a = 'cbbd'
a = 'abbbb'
# a = 'bb'
# a = "ac"
solution = Solution()
print(solution.longestPalindrome(a))
# BF -> 7084ms
# def isPalindrome(self, s: str):
#     for i in range(int(len(s) / 2)):
#         if s[i] != s[len(s) - 1 - i]:
#             return False
#     return True

# if len(s) <= 1:
#     return s
# maxLength = -1
# result = ""
# for i in range(len(s) - 1):
#     for j in range(i + 1, len(s) + 1):
#         subS = s[i:j]
#         if len(subS) > maxLength:
#             if self.isPalindrome(subS):
#                 maxLength = max(maxLength, len(subS))
#                 if len(subS) == maxLength:
#                     result = subS
# return result

# BF -> 5166ms
# if len(s) <= 1:
#     return s
#
# maxLength = -1
# maxS = ""
# for i in range(len(s) - 1):
#     for j in range(i, len(s)):
#         subS = s[i:j + 1]
#         if len(subS) > maxLength and subS == subS[::-1]:
#             maxLength = len(subS)
#             maxS = subS
# return maxS

# Expand Around Center -> 238ms
# if len(s) <= 1:
#     return s
#
# maxS = s[0]
#
#
# def expand(left, right):
#     while left >= 0 and right < len(s) and s[left] == s[right]:
#         left -= 1
#         right += 1
#     return s[left + 1:right]
#
#
# for i in range(1, len(s)):
#     odd = expand(i, i)
#     even = expand(i - 1, i)
#
#     if len(odd) > len(maxS):
#         maxS = odd
#
#     if len(even) > len(maxS):
#         maxS = even
#
# return maxS


# DP -> 2289
#         if len(s) <= 1:
#             return s
#
#         maxLength = -1
#         maxSubString = s[0]
#         dp = [[False for _ in range(len(s))] for _ in range(len(s))]
#         for i in range(len(s)):
#             dp[i][i] = True
#             for j in range(i):
#                 # i - j <= 2 => xx, xyx
#                 if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1]):
#                     dp[j][i] = True
#                     if i - j + 1 > maxLength:
#                         maxLength = i - j + 1
#                         maxSubString = s[j:i + 1]
#         return maxSubString
