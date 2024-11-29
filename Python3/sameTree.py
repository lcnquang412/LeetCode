class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack1 = [p]
        stack2 = [q]
        while True:
            if not stack1 or not stack2:
                break
            if p is None and q or p and q is None:
                return False
            elif p is None and q is None:
                p = stack1.pop()
                q = stack2.pop()
                continue
            elif p.val != q.val:
                return False
            stack1.append(p.left)
            stack1.append(p.right)
            stack2.append(q.left)
            stack2.append(q.right)
            p = stack1.pop()
            q = stack2.pop()
        return True


# a1 = TreeNode(1)
# a2 = TreeNode(2)
# a3 = TreeNode(3)
# a1.left = a2
# a1.right = a3
#
# b1 = TreeNode(1)
# b2 = TreeNode(2)
# b3 = TreeNode(3)
# b1.left = b2
# b1.right = b3

a1 = TreeNode(1)
a2 = TreeNode(2)
a1.left = a2

b1 = TreeNode(1)
b2 = TreeNode(2)
b1.right = b2

solution = Solution()
print(solution.isSameTree(a1, b1))

# Recursive
# def __init__(self):
#         self.result = True
#
# def inorder(self, p: TreeNode, q: TreeNode):
#     if not self.result:
#         return
#     if p is None or q is None:
#         if p is None and q or p and q is None:
#             self.result = False
#         return
#     self.inorder(p.left, q.left)
#     if p.val != q.val:
#         self.result = False
#         return
#     self.inorder(p.right, q.right)
#
# def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#     self.inorder(p, q)
#     return self.result
