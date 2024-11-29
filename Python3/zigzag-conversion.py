import math


def printArr2Dim(arr):
    for i in range(len(arr)):
        print('\n')
        print(arr[i])


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if length < numRows or numRows == 1:
            return s
        result = ''
        if numRows == 2:
            index = 0
            subResult = ''
            for char in s:
                if index % 2 == 1:
                    subResult += char
                else:
                    result += char
                index += 1
            return result + subResult
        mid = numRows - 2
        numCols = math.ceil((length - numRows) / (numRows + mid)) * (mid + 1) + 1
        table = [['' for _ in range(numCols)] for _ in range(numRows)]
        i = 0
        j = 0
        isMainCol = True
        for char in s:
            table[i][j] = char
            if isMainCol:
                i += 1
                if i == numRows:
                    j += 1
                    i -= 2
                    isMainCol = False
            else:
                i -= 1
                if i == 0:
                    j += 1
                    i = 0
                    isMainCol = True
        # printArr2Dim(table)

        for i in range(numRows):
            result += ''.join(table[i])
        return result


a = 'PAYPALISHIRING'
b = 3
a = 'PAYPALISHIRING'
b = 4
a = 'A'
b = 1
a = 'ABCDE'
b = 2
solution = Solution()
print(solution.convert(a, b))

# BF: 264
# length = len(s)
# if length < numRows or numRows == 1:
#     return s
# result = ''
# if numRows == 2:
#     index = 0
#     subResult = ''
#     for char in s:
#         if index % 2 == 1:
#             subResult += char
#         else:
#             result += char
#         index += 1
#     return result + subResult
# mid = numRows - 2
# numCols = math.ceil((length - numRows) / (numRows + mid)) * (mid + 1) + 1
# table = [['' for _ in range(numCols)] for _ in range(numRows)]
# i = 0
# j = 0
# isMainCol = True
# for char in s:
#     table[i][j] = char
#     if isMainCol:
#         i += 1
#         if i == numRows:
#             j += 1
#             i -= 2
#             isMainCol = False
#     else:
#         i -= 1
#         if i == 0:
#             j += 1
#             i = 0
#             isMainCol = True
# # printArr2Dim(table)
#
# for i in range(numRows):
#     result += ''.join(table[i])
# return result
