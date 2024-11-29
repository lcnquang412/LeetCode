class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        if length < 2:
            return False
        sNew = s * 2
        sNew = sNew[1:len(sNew) - 1]
        return sNew.count(s) > 0


a = "abab"
a = "aba"
a = "abcabcabcabc"
a = "bb"
solution = Solution()
print(solution.repeatedSubstringPattern(a))

# loop
#         length = len(s)
#         lengthReduce = length // 2
#         if length < 2:
#             return False
#         for i in range(lengthReduce):
#             template = s[0:lengthReduce - i]
#             if length % len(template) == 0:
#                 quantity = length / len(template)
#                 templateStr = template * int(quantity)
#                 if templateStr == s:
#                     return True
#         return False
