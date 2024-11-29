class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


solution = Solution()
print(solution.strStr("sad", "ad"))

# Original
# return haystack.find(needle)

# Other Solution
# for i in range(len(haystack) - len(needle) + 1):
#     if haystack[i:i + len(needle)] == needle:
#         return i
# return -1
