class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        length = len(nums)
        total = length * (length + 1) / 2
        totalNums = 0
        for num in nums:
            totalNums += num
        return int(total - totalNums)


a = [3, 0, 1]
a = [0, 1]
# a = [9, 6, 4, 2, 3, 5, 7, 0, 1]
solution = Solution()
print(solution.missingNumber(a))
