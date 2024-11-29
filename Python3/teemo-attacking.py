class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        if len(timeSeries) == 1:
            return duration
        prev = timeSeries[0]
        nextT = prev + duration - 1
        result = 0
        for i in range(1, len(timeSeries)):
            t = timeSeries[i]
            if t > nextT:
                result += duration
            else:
                result += t - prev
            nextT = t + duration - 1
            prev = t
        return result + duration


a = [1, 4]
b = 2
# a = [1, 2]
# b = 2
solution = Solution()
print(solution.findPoisonedDuration(a, b))
