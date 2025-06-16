class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        length = len(nums)
        count = 1
        maxCount = 1
        for i in range(1, length):
            if nums[i - 1] < nums[i]:
                count += 1
            else:
                maxCount = max(count, maxCount)
                count = 1
        return max(count, maxCount)


# a = [1, 3, 5, 4, 7]
a = [2, 2, 2, 2, 2]
a = [1, 3, 5, 7]
solution = Solution()
print(solution.findLengthOfLCIS(a))
