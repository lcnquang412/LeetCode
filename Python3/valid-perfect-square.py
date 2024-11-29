import math


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        tmp = math.sqrt(num)
        return tmp - math.floor(tmp) == 0


a = 16
solution = Solution()
print(solution.isPerfectSquare(a))
# Original
#         if num == 1:
#             return True
#         if num == 2 or num == 3:
#             return False
#         tmp = 4
#         index = 3
#         while tmp <= num:
#             if tmp == num:
#                 return True
#             tmp = index ** 2
#             index += 1
#         return False
