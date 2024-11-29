class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        mapping = {}
        maxCount = -1
        for num in nums:
            if num % 2 == 0:
                if num in mapping:
                    mapping[num] += 1
                else:
                    mapping[num] = 1
                maxCount = max(maxCount, mapping[num])

        minKey = 100001
        for key in mapping:
            if mapping[key] == maxCount:
                minKey = min(minKey, key)
        return minKey if minKey != 100001 else -1


a = [0, 1, 2, 2, 4, 4, 1]
a = [4, 4, 4, 9, 2, 4]
a = [29, 47, 21, 41, 13, 37, 25, 7]
solution = Solution()
print(solution.mostFrequentEven(a))
