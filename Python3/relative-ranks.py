class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        result = []
        scoreSorted = score.copy()
        scoreSorted.sort(reverse=True)
        hashMap = {}
        for index in range(len(scoreSorted)):
            s = scoreSorted[index]
            if index == 0:
                hashMap[s] = "Gold Medal"
            elif index == 1:
                hashMap[s] = "Silver Medal"
            elif index == 2:
                hashMap[s] = "Bronze Medal"
            else:
                hashMap[s] = f"{index + 1}"

        for s in score:
            result.append(hashMap[s])
        return result


# a = [5, 4, 3, 2, 1]
a = [10, 3, 8, 9, 4]
solution = Solution()
print(solution.findRelativeRanks(a))
