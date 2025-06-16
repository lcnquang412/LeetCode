class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        leftTotal = 0
        for i in range(len(nums)):
            num = nums[i]
            rightTotal = total - leftTotal - num
            if rightTotal == leftTotal:
                return i
            leftTotal += num
        return -1


a = [1, 7, 3, 6, 5, 6]
a = [1, 2, 3]
solution = Solution()
print(solution.pivotIndex(a))
