class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        resultPrev = 0
        result = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if resultPrev + num > result:
                tmp = result
                result = resultPrev + num
                resultPrev = tmp
            else:
                resultPrev = result
        return result


a = [1, 2, 3, 1]
a = [2, 7, 9, 3, 1]
a = [1]
solution = Solution()
print(solution.rob(a))
