class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:



a = [-1, 0, 1, 2, -1, -4]
# a = [0, 0, 0]
a = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
solution = Solution()
print(solution.threeSum(a))

# TLE
# if len(nums) < 3:
#     return []
# hashMap = {}
# resultHashMap = {}
# markHashMap = {}
# for i in range(len(nums)):
#     num = nums[i]
#     if num not in hashMap:
#         hashMap[num] = [i]
#     else:
#         hashMap[num].append(i)
# for i in range(len(nums) - 1):
#     for j in range(i + 1, len(nums)):
#         remain = (nums[i] + nums[j]) * -1
#         if remain in hashMap:
#             for k in hashMap[remain]:
#                 if k != i and k != j:
#                     tmp = [nums[i], nums[j], nums[k]]
#                     tmp.sort()
#                     resultHashMap[f'{tmp[0]}#{tmp[1]}#{tmp[2]}'] = True
#
# result = []
# for key in resultHashMap.keys():
#     tmp = key.split('#')
#     tmp = [int(item) for item in tmp]
#     result.append(tmp)
#
# return result


# TLE
# if len(nums) < 3:
#     return []
# hashMap = {}
# for i in range(len(nums) - 1):
#     left = nums[i]
#     for j in range(i + 1, len(nums)):
#         right = nums[j]
#         total = left + right
#         key = f'{left}#{right}'
#         if right < left:
#             key = f'{right}#{left}'
#         if total not in hashMap:
#             hashMap[total] = {
#                 key: [i, j]
#             }
#         elif key not in hashMap[total]:
#             hashMap[total][key] = [i, j]
#
# trace = {}
# resultTmp = []
# for index in range(len(nums)):
#     i = len(nums) - 1 - index
#     negativeNum = nums[i] * -1
#     if negativeNum in hashMap and negativeNum not in trace:
#         for key in hashMap[negativeNum].keys():
#             if i not in hashMap[negativeNum][key]:
#                 trace[negativeNum] = True
#                 resultTmp.append(f'{key}#{nums[i]}')
#
# resultTmp2 = {}
# for element in resultTmp:
#     arr = element.split("#")
#     arr.sort()
#     key = '#'.join(arr)
#     if key not in resultTmp2:
#         resultTmp2[key] = True
#
# result = []
# for key in resultTmp2.keys():
#     arr = key.split("#")
#     result.append([int(element) for element in arr])
#
# # print(hashMap)
# # print(resultTmp)
# # print(resultTmp2)
# return result