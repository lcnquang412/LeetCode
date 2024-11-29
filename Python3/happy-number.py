class Solution:
    def __init__(self):
        self.hashMap = {}

    def checkHappyNumber(self, n: str):
        if n == '1':
            return True
        if n in self.hashMap:
            return False
        else:
            self.hashMap[n] = True
        newNumber = 0
        for char in n:
            newNumber += int(char) ** 2
        return self.checkHappyNumber(f'{newNumber}')

    def isHappy(self, n: int) -> bool:
        self.hashMap = {}
        return self.checkHappyNumber(f'{n}')


a = 19
# a = 2
solution = Solution()
print(solution.isHappy(a))
