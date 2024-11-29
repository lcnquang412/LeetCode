class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.hashMap = {}

    def traverse(self, root: TreeNode):
        if root.val in self.hashMap:
            self.hashMap[root.val] += 1
        else:
            self.hashMap[root.val] = 1
        if root.left is None and root.right is None:
            return

        if root.left:
            self.traverse(root.left)
        if root.right:
            self.traverse(root.right)

    def findMode(self, root: TreeNode) -> list[int]:
        self.traverse(root)
        maxCount = -1
        for key in self.hashMap:
            maxCount = max(maxCount, self.hashMap[key])

        result = []
        for key in self.hashMap:
            if self.hashMap[key] == maxCount:
                result.append(key)
        return result


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(2)
a1.right = a2
a2.left = a3
solution = Solution()
print(solution.findMode(a1))
