class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        num1 = 0
        num2 = 1
        for i in range(1, n):
            tmp = num2
            num2 = num1 + num2
            num1 = tmp
        return num2


a = 4
solution = Solution()
print(solution.fib(a))
