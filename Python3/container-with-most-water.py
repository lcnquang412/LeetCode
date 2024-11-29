class Solution:
    def maxArea(self, height: list[int]) -> int:
        if len(height) == 1:
            return 0
        result = 0
        right = len(height) - 1
        left = 0
        while left <= right:
            if height[left] < height[right]:
                result = max(result, (right - left) * height[left])
                left += 1
            else:
                result = max(result, (right - left) * height[right])
                right -= 1
        return result


a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# a = [1, 1]
solution = Solution()
print(solution.maxArea(a))
