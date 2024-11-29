class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        print(nums)
        return j


a = [3, 2, 2, 3]
b = 3
a = [0, 1, 2, 2, 3, 0, 4, 2]
b = 2
a = [0, 1, 2, 2, 3, 0, 4, 2]
b = 2
solution = Solution()
print(solution.removeElement(a, b))

# Original
# j = 0
# count = 0
# lenth = len(nums)
# for i in range(0, lenth):
#     # last = lenth - 1 - i
#     if nums[i] == val and nums[j] != val:
#         j = i
#     if nums[i] != val and nums[j] == val:
#         nums[j] = nums[i]
#         nums[i] = val
#         j += 1
#         count += 1
#     print(nums)
# return count
