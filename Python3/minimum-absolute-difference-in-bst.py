class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.MIN = 1000001

    def getBest(self, root, side):
        if side == 'right':
            if root.right:
                return self.getBest(root.right, 'right')
        else:
            if root.left:
                return self.getBest(root.left, 'left')
        return root.val

    def traverse(self, root):
        if root.left is None and root.right is None:
            return

        if root.left:
            if root.left.right:
                self.MIN = min(self.MIN, abs(root.val - self.getBest(root.left, 'right')))
            else:
                self.MIN = min(self.MIN, abs(root.val - root.left.val))
            self.traverse(root.left)
        if root.right:
            if root.right.left:
                self.MIN = min(self.MIN, abs(root.val - self.getBest(root.right, 'left')))
            else:
                self.MIN = min(self.MIN, abs(root.val - root.right.val))
            self.traverse(root.right)

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.MIN


a1 = TreeNode(4)
a2 = TreeNode(2)
a3 = TreeNode(6)
a4 = TreeNode(1)
a5 = TreeNode(3)
a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5

# a1 = TreeNode(1)
# a2 = TreeNode(0)
# a3 = TreeNode(48)
# a4 = TreeNode(12)
# a5 = TreeNode(49)
# a1.left = a2
# a1.right = a3
# a3.left = a4
# a3.right = a5

# a1 = TreeNode(96)
# a2 = TreeNode(12)
# a3 = TreeNode(13)
# a4 = TreeNode(52)
# a5 = TreeNode(29)
# a1.left = a2
# a2.right = a3
# a3.right = a4
# a4.left = a5

solution = Solution()
print(solution.getMinimumDifference(a1))
