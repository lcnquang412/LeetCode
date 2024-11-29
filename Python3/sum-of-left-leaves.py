class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def traverse(self, root: TreeNode, side: str):
        if root.left is None and root.right is None:
            if side == 'left':
                self.result += root.val
            return
        if root.left:
            self.traverse(root.left, 'left')
        if root.right:
            self.traverse(root.right, 'right')

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.traverse(root, 'mid')
        return self.result


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a1.left = a2
a1.right = a3
a2.left = a4
solution = Solution()
print(solution.sumOfLeftLeaves(a1))
