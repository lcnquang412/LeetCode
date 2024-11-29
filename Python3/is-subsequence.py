class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        iT = 0
        iS = 0
        while iT < len(t) and iS < len(s):
            if s[iS] == t[iT]:
                iS += 1
            iT += 1
        return iS == len(s)


a = "abc"
b = "ahbgdc"
# a = "axc"
# b = "ahbgdc"
solution = Solution()
print(solution.isSubsequence(a, b))

# Brute Force
#         if s == "":
#             return True
#         tPool = [""]
#         for char in t:
#             tmp = []
#             for element in tPool:
#                 newElement = f'{element}{char}'
#                 if newElement == s:
#                     return True
#                 tmp.append(element)
#                 tmp.append(newElement)
#             tPool = tmp
#         return False

# Recursive
#     def traverse(self, s: str, t: str, n: int, m: int):
#         if n == 0:
#             return True
#         if m == 0:
#             return False
#         if s[n - 1] == t[m - 1]:
#             return self.traverse(s, t, n - 1, m - 1)
#         else:
#             return self.traverse(s, t, n, m - 1)
#
#     def isSubsequence(self, s: str, t: str) -> bool:
#         return self.traverse(s, t, len(s), len(t))
