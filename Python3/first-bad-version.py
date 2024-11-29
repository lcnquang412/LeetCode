import math


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(version: int) -> bool:
    return True


class Solution:
    def __init__(self):
        self.result = 1

    def checkBadVersion(self, left, midFloat, right):
        mid = int(midFloat)
        if mid <= left or mid >= right:
            if isBadVersion(mid):
                return mid
            return self.result
        if isBadVersion(mid):
            self.result = mid
            return self.checkBadVersion(left, left + math.floor((mid - left) / 2), mid)
        else:
            return self.checkBadVersion(mid, mid + math.ceil((right - mid) / 2), right)

    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 1 if isBadVersion(1) else 2
        return self.checkBadVersion(1, 1 + (n - 1) / 2, n)
