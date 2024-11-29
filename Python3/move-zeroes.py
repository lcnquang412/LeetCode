class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        start = -1
        for i in range(len(nums)):
            num = nums[i]
            if num != 0:
                if start != -1:
                    nums[start] = nums[i]
                    nums[i] = 0
                    start += 1
            else:
                if start == -1:
                    start = i
        return nums


a = [0, 1, 0, 3, 12]
# a = [0]
solution = Solution()
print(solution.moveZeroes(a))

# BF
#         arrIndexZero = []
#         length = len(nums)
#         for i in range(length):
#             if nums[i] == 0:
#                 arrIndexZero.append(i)
#
#         for i in range(len(arrIndexZero)):
#             indexZero = arrIndexZero[i]
#             for j in range(indexZero, length):
#                 if indexZero != j and nums[j] != 0:
#                     nums[indexZero] = nums[j]
#                     nums[j] = 0
#                     indexZero = j
#         return nums
