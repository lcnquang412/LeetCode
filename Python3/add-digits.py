class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9


a = 38
# a = 0
solution = Solution()
print(solution.addDigits(a))

# Recursive
#         numStr = f'{num}'
#         length = len(numStr)
#         if len(numStr) == 1:
#             return int(numStr)
#
#         total = 0
#         for i in range(length):
#             total += int(numStr[i])
#         return self.addDigits(total)
