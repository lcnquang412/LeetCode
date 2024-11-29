class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 or list1.val is None:
            return list2
        if not list2 or list2.val is None:
            return list1

        result = None
        currentNode = None
        arrValue = []
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    currentNode = list1
                    list1 = list1.next
                else:
                    currentNode = list2
                    list2 = list2.next
            elif list1:
                currentNode = list1
                list1 = list1.next
            elif list2:
                currentNode = list2
                list2 = list2.next

            if currentNode:
                arrValue.append(currentNode.val)

        arrValueLen = len(arrValue)
        for i in range(len(arrValue)):
            element = arrValue[arrValueLen - 1 - i]
            if not result:
                result = ListNode(element)
            else:
                result = ListNode(element, result)

        return result


solution = Solution()
# a1 = ListNode(1)
# a2 = ListNode(2)
# a3 = ListNode(4)
# a1.next = a2
# a2.next = a3
# b1 = ListNode(1)
# b2 = ListNode(3)
# b3 = ListNode(4)
# b1.next = b2
# b2.next = b3

a1 = ListNode(-6)
a2 = ListNode(-5)
a3 = ListNode(6)
a4 = ListNode(6)
a5 = ListNode(7)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
b1 = ListNode(0)


def printLL(target: ListNode):
    while target:
        print(target.val)
        target = target.next


printLL(solution.mergeTwoLists(a1, b1))
