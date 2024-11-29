class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def travel(self, root: TreeNode, depth: int):
        if root is None:
            return depth
        left = self.travel(root.left, depth + 1)
        right = self.travel(root.right, depth + 1)
        return max(left, right)

    def maxDepth(self, root: TreeNode) -> int:
        return self.travel(root, 0)


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a1.left = a2
a1.right = a3
a2.left = a4
# a4.right = a5
solution = Solution()
print(solution.maxDepth(a1))

# Original
# def __init__(self):
#     self.max = -1
#
# def travel(self, root: TreeNode, depth: int):
#     if root is None:
#         if depth > self.max:
#             self.max = depth
#         return
#     self.travel(root.left, depth + 1)
#     self.travel(root.right, depth + 1)
#
# def maxDepth(self, root: TreeNode) -> int:
#     self.travel(root, 0)
#     return self.max
