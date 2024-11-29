class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False


a1 = ListNode(3)
a2 = ListNode(2)
a3 = ListNode(0)
a4 = ListNode(4)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a2
solution = Solution()
print(solution.hasCycle(a1))

# Original
#         mapping = {}
#         while head is not None:
#             idHead = id(head)
#             if idHead in mapping:
#                 return True
#             else:
#                 mapping[idHead] = 1
#             head = head.next
#         return False


# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 (15 -> 3)
# fast = 1
# slow = 1
#
# fast = 3
# slow = 2
#
# fast = 5
# slow = 3
#
# f = 7
# s = 4
#
# f = 9
# s = 5
#
# f = 11
# s = 6
#
# f = 13
# s = 7
#
# f = 15
# s = 8
#
# ======
#
# f = 2
# s = 9
#
# f = 4
# s = 10
#
# f = 6
# s = 11
#
# f = 8
# s = 12
#
# f = 10
# s = 13
#
# f = 12
# s = 15
#
# f = 14
# s = 1
#
# ======
#
# f = 1
# s = 2
#
# f = 3
# s = 3
