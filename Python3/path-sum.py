class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.isExisted = False
        self.targetSum = 0

    def travel(self, root: TreeNode, total: int):
        if root.left is None and root.right is None:
            if total + root.val == self.targetSum:
                self.isExisted = True
            return
        if self.isExisted:
            return
        if root.left is not None:
            self.travel(root.left, total + root.val)
        # print(f'Left {root.val}: {total + root.val}')
        if root.right is not None:
            self.travel(root.right, total + root.val)
        # print(f'Right {root.val}: {total + root.val}')
        return

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        elif root.left is None and root.right is None:
            return root.val == targetSum
        self.targetSum = targetSum
        self.travel(root, 0)
        return self.isExisted


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.left = a2
a1.right = a3

# a1 = TreeNode(1)
# a2 = TreeNode(2)
# a3 = TreeNode(3)
# a4 = TreeNode(4)
# a5 = TreeNode(5)
# a1.left = a2
# a2.left = a3
# a3.left = a4
# a4.left = a5

b = 4
solution = Solution()
print(solution.hasPathSum(a1, b))
