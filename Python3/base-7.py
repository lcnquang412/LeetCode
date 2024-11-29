class Solution:
    def convertToBase7(self, num: int) -> str:
        negative = False
        result = ""
        if num < 0:
            negative = True
        remaining = abs(num)
        while remaining > 6:
            result = f'{remaining % 7}{result}'
            remaining = int(remaining / 7)
        result = f'{remaining}{result}'
        return result if not negative else f'-{result}'


a = 100
# a = -7
a = -1000000
solution = Solution()
print(solution.convertToBase7(a))
