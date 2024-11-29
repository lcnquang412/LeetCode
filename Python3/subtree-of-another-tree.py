class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = False
        self.subRoot = None
        self.found = False

    def traverseSub(self, root: TreeNode, subRoot: TreeNode):
        # print(f'Here {id(root)}:{root.val} {id(subRoot)}:{subRoot.val}')

        if (root.left is None and root.right is None) or not self.found:
            if subRoot.left is not None or subRoot.right is not None:
                self.found = False
            return
        if root.left is not None:
            if subRoot.left is not None and root.left.val == subRoot.left.val:
                self.traverseSub(root.left, subRoot.left)
            else:
                self.found = False
                return
        elif subRoot.left is not None:
            self.found = False
            return

        if root.right is not None:
            if subRoot.right is not None and root.right.val == subRoot.right.val:
                self.traverseSub(root.right, subRoot.right)
            else:
                self.found = False
                return
        elif subRoot.right is not None:
            self.found = False
            return
        if self.found and id(subRoot) == id(self.subRoot):
            self.result = True

    def traverse(self, root: TreeNode, subRoot: TreeNode):
        if self.result:
            return
        if root.right is None and root.left is None:
            if subRoot.right is None and subRoot.left is None:
                print(f'Here {root.val} {subRoot.val}')
                self.result = root.val == subRoot.val
            return
        if root.val == subRoot.val:
            print(f'======')
            self.found = True
            self.traverseSub(root, subRoot)
        if root.right is not None:
            self.traverse(root.right, subRoot)
        if root.left is not None:
            self.traverse(root.left, subRoot)

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root is None or subRoot is None:
            return False
        if (root.left is None and root.right is None) and (subRoot.left is None and subRoot.right is None):
            return root.val == subRoot.val
        self.subRoot = subRoot
        self.traverse(root, subRoot)
        return self.result


a1 = TreeNode(3)
a2 = TreeNode(4)
a3 = TreeNode(5)
a4 = TreeNode(1)
a5 = TreeNode(2)
a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5

b1 = TreeNode(4)
b2 = TreeNode(1)
b3 = TreeNode(2)
b4 = TreeNode(1)
b1.left = b2
b1.right = b3
b2.left = b4

a1 = TreeNode(1)
a2 = TreeNode(1)
a3 = TreeNode(1)
a4 = TreeNode(2)
a1.right = a2
a2.right = a3
a3.left = a4

b1 = TreeNode(1)
b2 = TreeNode(1)
b3 = TreeNode(2)
b1.right = b2
b2.left = b3

a1 = TreeNode(1)
a2 = TreeNode(1)
a1.left = a2

b1 = TreeNode(1)

solution = Solution()
print(solution.isSubtree(a1, b1))
