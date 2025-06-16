class Solution:
    class Tracking:
        def __init__(self, count, firstIndex):
            self.count = count
            self.firstIndex = firstIndex
            self.lastIndex = firstIndex

        def updateLast(self, lastIndex):
            self.lastIndex = lastIndex
            self.count += 1

        def getLength(self):
            return self.lastIndex - self.firstIndex

    def findShortestSubArray(self, nums: list[int]) -> int:
        tracking = {}
        maxCount = 1
        minLength = 50001
        if len(nums) == 1:
            return 1
        for i in range(len(nums)):
            num = nums[i]
            if num in tracking:
                tracking[num].updateLast(i)
                if tracking[num].count >= maxCount:
                    maxCount = tracking[num].count
            else:
                tracking[num] = self.Tracking(1, i)

        for num in tracking:
            if tracking[num].count == maxCount:
                length = tracking[num].getLength()
                if length < minLength:
                    minLength = length
        return minLength + 1


a = [1, 2, 2, 3, 1]
# a = [1, 2, 2, 3, 1, 4, 2]
# a = [2, 1]
solution = Solution()
print(solution.findShortestSubArray(a))
