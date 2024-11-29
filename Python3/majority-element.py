class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        result = 0
        count = 0
        for num in nums:
            if count == 0:
                result = num

            count += 1 if result == num else -1
        return result


a = [2, 2, 1, 1, 1, 2, 2]
solution = Solution()
print(solution.majorityElement(a))

# Hash
#         mapping = {}
#         maxNum = 0
#         result = 0
#         for num in nums:
#             if num in mapping:
#                 mapping[num] += 1
#             else:
#                 mapping[num] = 1
#             if mapping[num] > maxNum:
#                 maxNum = mapping[num]
#                 result = num
#         return result
