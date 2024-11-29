import math


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while True:
            mid = left + math.floor((right - left) / 2)
            numMid = nums[mid]
            print(f'{left} - {mid} ({numMid}) - {right}')
            if mid <= left or mid >= right:
                result = -1
                if target > nums[right]:
                    result = right + 1
                elif target < nums[left]:
                    result = left - 1
                else:
                    if target > numMid:
                        result = mid + 1
                    else:
                        result = mid - 1
                if result < 0:
                    result = 0
                return result

            if numMid == target:
                return mid
            elif numMid > target:
                right = mid
            elif numMid < target:
                left = mid


a = [1, 3, 5, 6]
b = 0
solution = Solution()
print(solution.searchInsert(a, b))
