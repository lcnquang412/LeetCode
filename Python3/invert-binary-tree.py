class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printLL(root: TreeNode):
    if root is None:
        return
    print(root.val)
    printLL(root.left)
    printLL(root.right)


class Solution:
    def __init__(self):
        self.resultRoot = None

    def traverse(self, root: TreeNode, result: TreeNode):
        if root is None:
            return
        if root.right:
            result.left = TreeNode(root.right.val)
            self.traverse(root.right, result.left)
        if root.left:
            result.right = TreeNode(root.left.val)
            self.traverse(root.left, result.right)

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        result = TreeNode(root.val)
        self.resultRoot = result
        self.traverse(root, result)
        return self.resultRoot


a1 = TreeNode(4)
a2 = TreeNode(2)
a3 = TreeNode(7)
a4 = TreeNode(1)
a5 = TreeNode(3)
a6 = TreeNode(6)
a7 = TreeNode(9)
a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5
a3.left = a6
a3.right = a7
solution = Solution()
printLL(a1)
print('======')
printLL(solution.invertTree(a1))
