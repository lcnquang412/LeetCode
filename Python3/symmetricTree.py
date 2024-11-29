class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubSymmetric(self, left: TreeNode, right: TreeNode):
        if left is None or right is None:
            return left == right
        return left.val == right.val and self.isSubSymmetric(left.left, right.right) and self.isSubSymmetric(left.right,
                                                                                                             right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root.left is None or root.right is None:
            return root.left == root.right

        return self.isSubSymmetric(root.left, root.right)


# a1 = TreeNode(1)
# a2 = TreeNode(2)
# a3 = TreeNode(2)
# a4 = TreeNode(3)
# a5 = TreeNode(4)
# a6 = TreeNode(4)
# a7 = TreeNode(3)
# a1.left = a2
# a1.right = a3
# a2.left = a4
# a2.right = a5
# a3.left = a6
# a3.right = a7

# a1 = TreeNode(1)
# a2 = TreeNode(2)
# a3 = TreeNode(2)
# a4 = TreeNode(3)
# a5 = TreeNode(3)
# a1.left = a2
# a1.right = a3
# a2.right = a4
# a3.right = a5

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(2)
a4 = TreeNode(2)
a5 = TreeNode(2)
a1.left = a2
a1.right = a3
a2.left = a4
a3.left = a5

solution = Solution()
print(solution.isSymmetric(a1))

# inOrder
#     def __init__(self):
#         self.values = []
#
#     def inOrder(self, root: TreeNode, side: str):
#         if root is None:
#             self.values.append({
#                 'side': side,
#                 'val': None
#             })
#             return
#         self.inOrder(root.left, '1')
#         self.values.append({
#             'side': side,
#             'val': root.val
#         })
#         self.inOrder(root.right, '0')
#
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if root.left is None and root.right is None:
#             return True
#         self.inOrder(root, '-1')
#         # print(self.values)
#         length = len(self.values)
#         halfLength = math.floor((length - 1) / 2)
#         for i in range(halfLength):
#             if self.values[i]["val"] != self.values[length - 1 - i]["val"] or \
#                     self.values[i]["side"] == self.values[length - 1 - i]["side"]:
#                 return False
#         return True
