class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if length <= numRows or numRows == 1:
            return s

        i = 0
        step = 0
        resultMatrix = [[] for _ in range(length)]
        for char in s:
            resultMatrix[i].append(char)
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            i += step

        result = ''
        for i in range(len(resultMatrix)):
            result += ''.join(resultMatrix[i])
        return result


a = 'PAYPALISHIRING'
b = 3
solution = Solution()
print(solution.convert(a, b))

# O(n) -> 11ms
#         length = len(s)
#         if length < numRows or numRows == 1:
#             return s
#
#         result = []
#
#         def appendResult(i: int):
#             j = 0
#             while True:
#                 step = 2 * (numRows - 1) * j
#                 # Left
#                 candidateIndex = i + step
#
#                 if candidateIndex > length - 1:
#                     break
#                 else:
#                     result.append(s[candidateIndex])
#                 # Right
#                 if 0 < i < numRows - 1:
#                     candidateIndex = i + 2 * (numRows - i - 1) + step
#                     if candidateIndex > length - 1:
#                         break
#                     else:
#                         result.append(s[candidateIndex])
#                 j += 1
#
#         for i in range(numRows):
#             appendResult(i)
#
#         return ''.join(result)
