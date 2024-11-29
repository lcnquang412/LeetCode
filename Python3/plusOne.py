class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        remember = 0
        length = len(digits)
        for i in range(length):
            if digits[length - 1 - i] == 9:
                digits[length - 1 - i] = 0
                remember = 1
            else:
                digits[length - 1 - i] += 1
                remember = 0
            if remember == 0:
                break
        if remember == 1:
            digits.insert(0, 1)
        return digits


a = [9]
solution = Solution()
print(solution.plusOne(a))
