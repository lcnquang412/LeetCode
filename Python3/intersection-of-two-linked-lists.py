class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        mapping = {}
        while headA is not None or headB is not None:
            if headA is not None:
                idHeadA = id(headA)
                if idHeadA in mapping:
                    return headA
                else:
                    mapping[idHeadA] = True
                headA = headA.next

            if headB is not None:
                idHeadB = id(headB)
                if idHeadB in mapping:
                    return headB
                else:
                    mapping[idHeadB] = True
                headB = headB.next
        return None


def printLL(node: ListNode):
    while node is not None:
        print(node.val)
        node = node.next


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a1.next = a2
a2.next = a3

b1 = ListNode(4)
b2 = ListNode(5)
b1.next = b2
b2.next = a2

# a1 = ListNode(1)
# b1 = ListNode(1)
solution = Solution()
c = solution.getIntersectionNode(a1, b1)
printLL(c)

# Original


# 2 point: Time limit
#         a, b = headA, headB
#         if a == b:
#             return a
#         while True:
#             if a is None and b is None:
#                 break
#             elif a is None:
#                 a = headA
#             elif b is None:
#                 b = headB
#             else:
#                 a = a.next
#                 b = b.next
#             if a == b:
#                 return a
#
#         return None
