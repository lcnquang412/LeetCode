class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def printLL(node: ListNode):
    while node is not None:
        print(node.val)
        node = node.next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            if head.val == val:
                return None
            else:
                return head
        tmp = head
        while tmp is not None and tmp.val == val:
            tmp = tmp.next
            head = tmp

        while tmp is not None and tmp.next is not None:
            if tmp.next.val == val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next

        return head


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(1)
a1.next = a2
a2.next = a3
a3.next = a4
b = 1
solution = Solution()
printLL(solution.removeElements(a1, b))
