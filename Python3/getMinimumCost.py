import math


class Solution:
    def getMinimumCost(self, arr: list[int]) -> int:
        max = -1
        left = 0
        total = 0
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) > max:
                max = abs(arr[i] - arr[i - 1])
                left = i - 1
        for i in range(len(arr) - 1):
            if i == left:
                total += math.floor(abs(arr[i] - arr[i + 1]) / 2) ** 2 + math.ceil(abs(arr[i] - arr[i + 1]) / 2) ** 2
            else:
                total += abs(arr[i] - arr[i + 1]) ** 2
        return total


a = [1, 3, 5, 2, 10]
solution = Solution()
print(solution.getMinimumCost(a))
