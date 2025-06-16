class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        pre1 = False
        for i in range(len(bits)):
            bit = bits[i]
            if bit == 0:
                if i == len(bits) - 1 and not pre1:
                    return True
                pre1 = False
            else:
                pre1 = not pre1
        return False


a = [1, 0, 0]
a = [1, 1, 1, 0]
solution = Solution()
print(solution.isOneBitCharacter(a))
