class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if nums is None:
            return None

        length = len(nums)
        if length == 0:
            return None
        elif length == 1:
            return [f'{nums[0]}']

        starNum = nums[0]
        prevNum = starNum
        result = []
        for i in range(1, length):
            num = nums[i]
            prevNum = nums[i - 1]
            if num - prevNum == 1:
                continue
            else:
                result.append(f'{starNum}->{prevNum}' if starNum != prevNum else f'{starNum}')
                starNum = nums[i]

        prevNum = nums.pop()
        result.append(f'{starNum}->{prevNum}' if starNum != prevNum else f'{starNum}')
        return result


a = [0, 1, 2, 4, 5, 7]
# a = [0, 2, 3, 4, 6, 8, 9]
solution = Solution()
print(solution.summaryRanges(a))
