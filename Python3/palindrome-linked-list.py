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
        self.result = True
        self.headStart = None

    def traverse(self, headEnd: ListNode):
        if headEnd is None:
            return
        self.traverse(headEnd.next)
        if not self.result:
            return
        if self.headStart.val != headEnd.val:
            self.result = False
            return
        self.headStart = self.headStart.next

    def isPalindrome(self, head: ListNode) -> bool:
        self.headStart = head
        self.traverse(head)
        return self.result


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(3)
a5 = ListNode(1)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
solution = Solution()
print(solution.isPalindrome(a1))
