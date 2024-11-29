class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0

    def traverse(self, root: TreeNode):
        if root is None:
            return
        self.count += 1
        self.countNodes(root.left)
        self.countNodes(root.right)

    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.left = a2
a1.right = a3
solution = Solution()
print(solution.countNodes(a1))
