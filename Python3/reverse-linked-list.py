class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def printLL(node: ListNode):
    while node is not None:
        print(node.val)
        node = node.next


class Solution:
    def __init__(self):
        self.headReversed = None
        self.headReversedTmp = None

    def reverse(self, head: ListNode):
        if head is None:
            return head
        self.reverse(head.next)
        if self.headReversed is None:
            self.headReversed = ListNode(head.val)
            self.headReversedTmp = self.headReversed
        else:
            self.headReversedTmp.next = ListNode(head.val)
            self.headReversedTmp = self.headReversedTmp.next

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        self.reverse(head)
        return self.headReversed


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a1.next = a2
a2.next = a3
solution = Solution()
printLL(solution.reverseList(a1))
