class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        length = len(nums) + 1
        trackingList = [0] * length
        result = [0, 0]
        for num in nums:
            trackingList[num] += 1
        for i in range(1, length):
            count = trackingList[i]
            if count != 1:
                if count == 2:
                    result[0] = i
                else:
                    result[1] = i
        return result


a = [2, 2]
solution = Solution()
print(solution.findErrorNums(a))
