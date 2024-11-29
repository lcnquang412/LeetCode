class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def traverse(self, root: TreeNode):
        if root.left is None and root.right is None:
            return root.val
        totalLeft = 0
        totalRight = 0
        if root.left:
            totalLeft += self.traverse(root.left)
        if root.right:
            totalRight += self.traverse(root.right)

        self.result += abs(totalLeft - totalRight)
        return totalLeft + totalRight + root.val

    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.traverse(root)
        return self.result


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.left = a2
a1.right = a3

# a1 = TreeNode(4)
# a2 = TreeNode(2)
# a3 = TreeNode(9)
# a4 = TreeNode(3)
# a5 = TreeNode(5)
# a6 = TreeNode(7)
# a1.left = a2
# a1.right = a3
# a2.left = a4
# a2.right = a5
# a3.right = a6

solution = Solution()
print(solution.findTilt(a1))
