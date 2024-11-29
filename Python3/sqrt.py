import math


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        if x < 4:
            return 1
        left = 2
        right = 46341
        while True:
            mid = left + math.floor((right - left) / 2)
            print(f'{left} {mid} {right}')
            if mid * mid == x:
                return mid
            if left * left <= x <= right * right and right - left == 1:
                return left
            elif mid * mid > x:
                right = mid
            elif mid * mid < x:
                left = mid

        return 0


solution = Solution()
print(solution.mySqrt(7))

# Built-in exponent function
# x ** 0.5
