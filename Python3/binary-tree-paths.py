class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []

    def traverse(self, root, result):
        if root.left is None and root.right is None:
            self.result.append(f'{result}{root.val}')
        if root.left:
            self.traverse(root.left, f'{result}{root.val}->')
        if root.right:
            self.traverse(root.right, f'{result}{root.val}->')

    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [f'{root.val}']
        self.traverse(root, "")
        return self.result


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(5)
a1.left = a2
a1.right = a3
a2.right = a4
solution = Solution()
print(solution.binaryTreePaths(a1))
