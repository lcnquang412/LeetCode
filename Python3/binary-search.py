import math


class Solution:
    def binarySearch(self, nums: list[int], target: int, left: int, right: int) -> int:
        if (left == right and nums[left] != target) or (left > right):
            return -1
        mid = left + math.floor((right - left) / 2)
        value = nums[mid]
        if target == value:
            return mid
        else:
            if target < value:
                return self.binarySearch(nums, target, left, mid - 1)
            else:
                return self.binarySearch(nums, target, mid + 1, right)

    def search(self, nums: list[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)


a = [-1, 0, 3, 5, 9, 12]
b = 9
# a = [-1, 0, 3, 5, 9, 12]
# b = 2
solution = Solution()
print(solution.search(a, b))
