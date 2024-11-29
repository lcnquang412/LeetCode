class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[j - 1]:
                nums[j] = nums[i]
                j += 1
        return j


a = [1, 1, 2]
a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
a = [0, 0, 0, 1, 1, 2, 3, 4, 4]
solution = Solution()
print(solution.removeDuplicates(a))

# Original
# hashMap = {}
# k = 0
# _CurrentIndex = 0
# _Array = []
# for i in range(len(nums)):
#     num = nums[i]
#     if num not in hashMap:
#         hashMap[num] = "1"
#         k += 1
#         if len(_Array) > 0:
#             _Min = min(_Array)
#             _MinIndex = _Array.index(_Min)
#             if _Min <= i:
#                 nums[_Array[_MinIndex]] = num
#                 _Array[_MinIndex] = i
#                 nums[i] = "_"
#     else:
#         nums[i] = "_"
#         _Array.append(i)
#     # print(_CurrentIndex)
#     # print(_Array)
#     # print(nums)
#     # print("===========")
# return k

# **************************************
# **************************************
# **************************************

# Queue (list)
# hashMap = {}
# k = 0
# queue = []
# for i in range(len(nums)):
#     num = nums[i]
#     if num not in hashMap:
#         hashMap[num] = "1"
#         k += 1
#         if len(queue) > 0:
#             if queue[0] <= i:
#                 nums[queue.pop(0)] = num
#                 nums[i] = "_"
#                 queue.append(i)
#     else:
#         nums[i] = "_"
#         queue.append(i)
# # print(nums)
# return k

# **************************************
# **************************************
# **************************************

# Queue (linked list) => Not good
# def printLL(self, node: Node):
#     while node is not None:
#         print(node.val)
#         node = node.next
#
# def removeDuplicates(self, nums: list[int]) -> int:
#     hashMap = {}
#     k = 0
#     queuell = LinkedList()
#     for i in range(len(nums)):
#         num = nums[i]
#         if num not in hashMap:
#             hashMap[num] = "1"
#             k += 1
#             if not queuell.isEmpty():
#                 queuellFirstValue = queuell.getValueOfFirst()
#                 if queuellFirstValue <= i:
#                     nums[queuellFirstValue] = num
#                     nums[i] = "_"
#                     queuell.append(i)
#                     queuell.removeFirst()
#         else:
#             nums[i] = "_"
#             queuell.append(i)
#     print(nums)
#     self.printLL(queuell.first)
#     return k
