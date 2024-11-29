class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.depthResult = 10001

    def travel(self, root: TreeNode, depth: int):
        if (root.left is None and root.right is None) or \
                depth >= self.depthResult:
            return depth
        if root.left is not None:
            left = self.travel(root.left, depth + 1)
        else:
            left = 100001
        if root.right is not None:
            right = self.travel(root.right, depth + 1)
        else:
            right = 100001
        self.depthResult = min(left, right)
        return self.depthResult

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.travel(root, 0) + 1


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.left = a2
a1.right = a3
solution = Solution()
print(solution.minDepth(a1))
