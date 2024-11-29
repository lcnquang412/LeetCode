class Solution:
    def countBits(self, n: int) -> list[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        result = [0, 1]
        for i in range(2, n + 1):
            result.append(bin(i).count('1'))
        return result


a = 12
solution = Solution()
print(solution.countBits(a))
# n*log(n)
#         if n == 0:
#             return [0]
#         elif n == 1:
#             return [0, 1]
#         result = [0, 1]
#         for i in range(2, n + 1):
#             tmp = i
#             count = 1
#             while tmp != 1:
#                 count += tmp % 2
#                 tmp = tmp >> 1
#             result.append(count)
#         return result
