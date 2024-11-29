class Solution:
    def getBits(self, n: int) -> str:
        if n == 1:
            return '1'
        return f'{n % 2}{self.getBits(n // 2)}'

    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        strBits = self.getBits(n)
        step = 31
        result = 0
        for char in strBits:
            if char == '1':
                result += 2 ** step
            step -= 1
        return result


a = 43261596
a = 0
a = 1
solution = Solution()
print(solution.reverseBits(a))
