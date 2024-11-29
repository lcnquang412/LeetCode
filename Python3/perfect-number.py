class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total = 1
        if num == 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                total += i + int(num / i)
        print(total)
        return total == num


a = 28
a = 7
a = 6
solution = Solution()
print(solution.checkPerfectNumber(a))
