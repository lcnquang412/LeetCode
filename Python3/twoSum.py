# Brute Force
# length = len(nums)
# for i in range(0, length - 1):
#     for j in range(i + 1, length):
#         if nums[i] + nums[j] == target:
#             return [i, j]
# return []

# Find
# length = len(nums)
# if length == 2:
#     return [0, 1]
#
# for i in range(length):
#     j = -1
#     try:
#         j = nums.index(target - nums[i])
#     except ValueError:
#         continue
#     if i != j:
#         return [i, j]
# return []

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pair_i = {}

        for i, num in enumerate(nums):
            if target - num in pair_i:
                return [i, pair_i[target - num]]
            pair_i[num] = i
        return []


a = [2, 5, 5, 11]
b = 10
solution = Solution()
print(solution.twoSum(a, b))
