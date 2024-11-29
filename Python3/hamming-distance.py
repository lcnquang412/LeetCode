class Solution:
    def __init__(self):
        self.result = 0

    def hammingDistance(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return self.result
        self.result += 1 if x % 2 != y % 2 else 0
        return self.hammingDistance(x >> 1, y >> 1)


a = 1
b = 4
a = 3
b = 1
solution = Solution()
print(solution.hammingDistance(a, b))
