class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        index = 0
        result = 0
        for i in range(int(len(nums) / 2)):
            result += nums[index]
            index += 2
        return result


a = [1, 4, 3, 2]
solution = Solution()
print(solution.arrayPairSum(a))
