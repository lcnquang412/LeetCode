import math


# Simulator
def guess(num: int) -> int:
    return 1


class Solution:
    def traverse(self, left, mid, right):
        if guess(mid) == 0:
            return mid
        elif guess(mid) == -1:
            return self.traverse(left, left + (mid - left) // 2, mid)
        else:
            return self.traverse(mid, mid + math.ceil((right - mid) / 2), right)

    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        return self.traverse(1, 1 + (n - 1) // 2, n)


a = 10
solution = Solution()
print(solution.guessNumber(10))
