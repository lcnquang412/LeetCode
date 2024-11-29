class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()


a = [1, 2, 3, 0, 0, 0]
b = 3
c = [2, 5, 6]
d = 3
solution = Solution()
solution.merge(a, b, c, d)
print(a)

# Original
# result = []
# if n == 0:
#     return
# if m == 0:
#     result = nums2
# else:
#     i = 0
#     j = 0
#     for k in range(len(nums1)):
#         # print(f'{i} {j}')
#         # print(result)
#         if j == n or (j < n and i < m and nums1[i] < nums2[j]):
#             result.append(nums1[i])
#             i += 1
#         elif i == m or (j < n and i < m and nums1[i] >= nums2[j]):
#             result.append(nums2[j])
#             j += 1
# for k in range(len(result)):
#     nums1[k] = result[k]
# return
