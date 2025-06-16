# max(a[n] * a[n-1] * a[n-2], a[0], a[1], a[n])


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        # === Sort ===
        # nums.sort()
        # n = len(nums)
        # return max(nums[n - 1] * nums[n - 2] * nums[n - 3], nums[0] * nums[1] * nums[n - 1])

        # === Greedy ===
        min1 = 1001
        min2 = 1001
        max1 = -1001
        max2 = -1001
        max3 = -1001
        for num in nums:
            if num < min1:
                min2 = min1
                min1 = num
            elif min1 <= num < min2:
                min2 = num

            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif max1 >= num > max2:
                max3 = max2
                max2 = num
            elif max2 >= num > max3:
                max3 = num
        return max(min1 * min2 * max1, max3 * max2 * max1)


a = [1, 2, 3, 4]
# a = [10, 3, 5, 6, 20]
# a = [-10, -3, -5, -6, -20]
# a = [1000, 1000, 1000]
# a = [-1, -2, -3]
solution = Solution()
print(solution.maximumProduct(a))
