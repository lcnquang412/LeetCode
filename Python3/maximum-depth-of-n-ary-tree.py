class Node:
    def __init__(self, val: int = None, children: list['Node'] = None):
        self.val = val
        self.children = children


class Solution:
    def traverse(self, root: 'Node', height: int):
        if not root.children:
            return height
        maxHeight = [-1]
        if root.children:
            for child in root.children:
                maxHeight.append(
                    self.traverse(child, height + 1)
                )
        return max(maxHeight)

    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        return self.traverse(root, 1)


a5 = Node(5, None)
a6 = Node(6, None)
a3 = Node(3, [a5, a6])
a2 = Node(2, None)
a4 = Node(4, None)
a1 = Node(1, [a3, a2, a4])
solution = Solution()
print(solution.maxDepth(a1))
