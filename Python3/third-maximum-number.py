class Solution:
    def __init__(self):
        self.MIN = -2 ** 31 - 1
        self.third = self.MIN
        self.second = self.MIN
        self.first = self.MIN

    def check(self, num):
        if num == self.first or num == self.second or num == self.third:
            return
        if num > self.third:
            self.third = num
            if self.second < self.third:
                tmp = self.third
                self.third = self.second
                self.second = tmp
                if self.first < self.second:
                    tmp = self.second
                    self.second = self.first
                    self.first = tmp

    def thirdMax(self, nums: list[int]) -> int:
        for num in nums:
            self.check(num)
        if self.third == self.MIN:
            return self.first
        else:
            return self.third


# a = [3, 2, 1]
a = [2, 2, 3, 1]
solution = Solution()
print(solution.thirdMax(a))
