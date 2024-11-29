class Node:
    def __init__(self, val: int = None, children: list['Node'] = None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.result = []

    def traverse(self, root: 'Node'):
        if root.children is not None:
            for child in root.children:
                self.traverse(child)
        self.result.append(root.val)

    def postorder(self, root: 'Node') -> list[int]:
        if root is None:
            return []
        if root.children is None:
            return [root.val]
        self.traverse(root)
        return self.result


a6 = Node(6, None)
a5 = Node(5, None)
a3 = Node(3, [a5, a6])
a2 = Node(2, None)
a4 = Node(4, None)
a1 = Node(1, [a3, a2, a4])

solution = Solution()
print(solution.postorder(a1))
