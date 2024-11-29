class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []

    def traverse(self, root: TreeNode):
        if not root:
            return
        self.traverse(root.left)
        self.result.append(root.val)
        self.traverse(root.right)

    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return None
        self.traverse(root)
        return self.result


solution = Solution()
# a1 = TreeNode(1)
# a2 = TreeNode(2)
# a3 = TreeNode(3)
# a1.right = a2
# a2.left = a3

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a6 = TreeNode(6)
a7 = TreeNode(7)
a8 = TreeNode(8)
a9 = TreeNode(9)
a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5
a5.left = a6
a5.right = a7
a3.right = a8
a8.left = a9
print(solution.inorderTraversal(a1))
