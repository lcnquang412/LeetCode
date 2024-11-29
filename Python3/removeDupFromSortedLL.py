class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val: int):
        node = ListNode(val)
        current = self.head
        if self.head is None:
            self.head = node
        else:
            while current.next is not None:
                current = current.next
            current.next = node

    def getHead(self):
        return self.head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        result = LinkedList()
        currentVal = -101

        while head is not None:
            if currentVal != head.val:
                currentVal = head.val
                result.append(head.val)
            head = head.next
        return result.getHead()


def printLL(head: ListNode):
    while head is not None:
        print(head.val)
        head = head.next


a1 = ListNode(1)
a2 = ListNode(1)
a3 = ListNode(2)
a1.next = a2
a2.next = a3
solution = Solution()
printLL(solution.deleteDuplicates(a1))
