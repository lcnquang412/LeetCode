class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        if area < 4:
            return [area, 1]
        length = int(area ** 0.5)
        for i in range(2, length + 1):
            right = length - i + 2
            if area % right == 0:
                return [int(area / right), right]
        return [area, 1]


a = 4
# a = 37
# a = 122122
solution = Solution()
print(solution.constructRectangle(a))
