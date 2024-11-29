class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = -1

    def travers(self, root: TreeNode, side: str, height: int):
        if root.left is None and root.right is None:
            return height
        leftHeight = 0
        rightHeight = 0
        if root.left:
            leftHeight = self.travers(root.left, side, height + 1)
        if root.right:
            rightHeight = self.travers(root.right, side, height + 1)
        # print("---")
        # print(f'{leftHeight} + {rightHeight} = {leftHeight + rightHeight - height}')
        self.result = max(self.result, leftHeight + rightHeight - height * 2)
        return max(leftHeight, rightHeight)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        leftHeight = 0
        rightHeight = 0
        if root.left:
            leftHeight = self.travers(root.left, 'left', 1)
        if root.right:
            rightHeight = self.travers(root.right, 'right', 1)
        return max(self.result, leftHeight + rightHeight)


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5
solution = Solution()
print(solution.diameterOfBinaryTree(a1))
