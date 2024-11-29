class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        numBin = bin(num).lstrip("0b")
        numBinList = list(numBin)
        for i in range(len(numBinList)):
            tmp = 1 if numBinList[len(numBinList) - 1 - i] == '0' else 0
            result += tmp * (2 ** i)

        return result


a = 5
a = 1
a = 2 ** 31
print(a)
solution = Solution()
print(solution.findComplement(a))
