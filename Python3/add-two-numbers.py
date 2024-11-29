class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def printLL(node: ListNode):
    while node is not None:
        print(node.val)
        node = node.next


class Solution:
    def traverse(self, l1: ListNode, l2: ListNode, remain: int):
        if l1 is None and l2 is None:
            if remain == 1:
                return ListNode(1)
            else:
                return None
        l1Val = 0 if l1 is None else l1.val
        l2Val = 0 if l2 is None else l2.val
        total = l1Val + l2Val + remain
        return ListNode(total % 10, self.traverse(
            None if l1 is None else l1.next,
            None if l2 is None else l2.next,
            int(total / 10)
        ))

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.traverse(l1, l2, 0)


a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)
a1.next = a2
a2.next = a3

b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

a1 = ListNode(0)
b1 = ListNode(0)

a1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
b1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

solution = Solution()
printLL(solution.addTwoNumbers(a1, b1))
