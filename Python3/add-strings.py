import math


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1Revert = list(num1)
        num2Revert = list(num2)
        remain = 0
        result = []
        maxLength = max(len(num1Revert), len(num2Revert))
        for i in range(maxLength):
            firstDigit = 0
            secondDigit = 0
            index1 = len(num1Revert) - 1 - i
            index2 = len(num2Revert) - 1 - i
            if index1 >= 0:
                firstDigit = int(num1[index1])
            if index2 >= 0:
                secondDigit = int(num2[index2])
            total = firstDigit + secondDigit + remain
            remain = math.floor(total / 10)
            result.append(f'{total % 10}')
        if remain == 1:
            result.append('1')
        result.reverse()
        return ''.join(result)


a = "11"
b = "123"
a = "456"
b = "77"
a = "0"
b = "0"
solution = Solution()
print(solution.addStrings(a, b))
