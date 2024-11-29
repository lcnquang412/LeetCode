class Solution:
    def findLHS(self, nums: list[int]) -> int:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        result = 0
        for num in list(hashMap.keys()):
            if num + 1 in hashMap:
                result = max(result, hashMap[num] + hashMap[num + 1])
        return result


a = [1, 3, 2, 2, 5, 2, 3, 7]
# a = [1, 2, 5, 6, 6]
# a = [1, 1, 1, 1]
# a = [1, 3, 5, 7, 9, 11, 13, 15, 17]
# a = [1, 2, 1, 3, 0, 0, 2, 2, 1, 3, 3]
# a = [1, 4, 1, 3, 1, -14, 1, -13]
a = [3, 2, 2, 3, 2, 1, 3, 3, 3, -2, 0, 3, 2, 1, 0, 3, 1, 0, 1, 3, 0, 3, 3]
solution = Solution()
print(solution.findLHS(a))

# Sort + Loop
# if len(nums) < 2:
#     return 0
# nums.sort()
# left = nums[0]
# right = -100000001
# count = 1
# countLeft = 1
# countRight = 0
# result = 0
# # print(nums)
# for i in range(1, len(nums)):
#     current = nums[i]
#     # print(f'=== {current} ===')
#     if current == left:
#         count += 1
#         countLeft += 1
#     elif current == left + 1:
#         count += 1
#         right = current
#         countRight += 1
#         result = max(result, count)
#     else:
#         if right != -100000001 and current == right + 1:
#             left = right
#             right = current
#             countLeft = countRight
#             count = countRight + 1
#             countRight = 1
#         else:
#             left = current
#             right = -100000001
#             countLeft = 1
#             count = 1
#             countRight = 0
#     # print(f'count: {count}')
# return result
