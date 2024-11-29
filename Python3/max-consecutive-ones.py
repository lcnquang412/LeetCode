class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        maxCount = -1
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0
        return max(maxCount, count)


a = [1, 1, 0, 1, 1, 1]
a = [1, 0, 1, 1, 0, 1]
solution = Solution()
print(solution.findMaxConsecutiveOnes(a))
