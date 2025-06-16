class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        maxValue = max(a)
        result = -1
        for i in range(len(nums)):
            num = nums[i]
            if num == maxValue:
                result = i
            elif num * 2 > maxValue:
                return -1
        return result


a = [3, 6, 1, 2]
# a = [1, 2, 3, 4]
solution = Solution()
print(solution.dominantIndex(a))
