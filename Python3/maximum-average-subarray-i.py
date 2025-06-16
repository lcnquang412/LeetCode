class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total = 0
        firstIndex = 0
        for i in range(k):
            total += nums[i]
        result: float = total / k
        for i in range(k, len(nums)):
            total += nums[i] - nums[firstIndex]
            firstIndex += 1
            result = total / k if total / k > result else result
        return result


# a = [1, 12, -5, -6, 50, 3]
# b = 4
a = [5]
b = 1
solution = Solution()
print(solution.findMaxAverage(a, b))
