import math


class Solution:
    def cal(self, n):
        return n * (n + 1) / 2

    def traverse(self, left, mid, right, n):
        midCalculated = self.cal(mid)
        print(f'{left} {mid} {right} => {midCalculated}')
        if midCalculated == n:
            return mid
        if midCalculated > n >= self.cal(mid - 1):
            return mid - 1
        if midCalculated > n:
            return self.traverse(left, left + (mid - left) // 2, mid, n)
        elif midCalculated < n:
            return self.traverse(mid, mid + math.ceil((right - mid) / 2), right, n)

    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        return self.traverse(1, 1 + (n - 1) // 2, n, n)


a = 4
solution = Solution()
print(solution.arrangeCoins(a))

# Brute Force
#         if n == 1:
#             return 1
#         tmp = 1
#         index = 2
#         while tmp <= n:
#             tmp = index * (index + 1) / 2
#             index += 1
#         return index - 1 if tmp == n else index - 2
