class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        def funcFilter(e):
            return e != 0

        result = []
        for i in range(len(nums) + 1):
            result.append(i)
        result[0] = 0
        for num in nums:
            result[num] = 0
        filtered = list(filter(funcFilter, result))
        return filtered


a = [4, 3, 2, 7, 8, 2, 3, 1]
solution = Solution()
print(solution.findDisappearedNumbers(a))

# Brute Force
#         result = []
#         for i in range(1, len(nums) + 1):
#             if i not in nums:
#                 result.append(i)
#         return result

# Hash
#         result = []
#         hashMap = {}
#         for num in nums:
#             if num not in hashMap:
#                 hashMap[num] = True
#         for i in range(1, len(nums) + 1):
#             if i not in hashMap:
#                 result.append(i)
#         return result
