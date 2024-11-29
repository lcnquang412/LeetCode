class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.traverse(root.right)
        self.result.append(root.val)

    def postorderTraversal(self, root: TreeNode) -> list[int]:
        self.traverse(root)
        return self.result


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.right = a2
a2.left = a3
solution = Solution()
print(solution.postorderTraversal(a1))
