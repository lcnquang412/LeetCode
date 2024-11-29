class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.isCorrect = True

    def travel(self, root: TreeNode, depth: int):
        if root is None or self.isCorrect is False:
            return depth
        left = self.travel(root.left, depth + 1)
        right = self.travel(root.right, depth + 1)
        # print(f'{root.val}: {left} - {right}')
        self.isCorrect &= abs(left - right) < 2
        return max(left, right)

    def isBalanced(self, root: TreeNode) -> bool:
        self.travel(root, 0)
        return self.isCorrect


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a1.left = a2
a1.right = a3
a3.right = a4
# a4.right = a5
solution = Solution()
print(solution.isBalanced(a1))
