import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        length = len(nums)
        if length == 0:
            return None
        mid = math.floor(length / 2)
        return TreeNode(
            nums[mid],
            self.sortedArrayToBST(nums[:mid]),
            self.sortedArrayToBST(nums[mid + 1:])
        )


def printLL(a: TreeNode, father: int, side: str):
    if a is None:
        return
    print(f'{father} - {side}: {a.val}')
    printLL(a.left, a.val, 'Left')
    printLL(a.right, a.val, 'Right')


a1 = [-10, -3, 0, 5, 9]
a1 = [0, 1, 2, 3, 4, 5]
solution = Solution()
printLL(solution.sortedArrayToBST(a1), None, 'Root')
