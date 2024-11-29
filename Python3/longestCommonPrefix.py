class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        length = len(strs)
        minLen = 300
        minIndex = -1
        for i in range(length):
            eLength = len(strs[i])
            if eLength < minLen:
                minLen = eLength
                minIndex = i
        if minLen == 0:
            return ""

        minValue = strs[minIndex]
        MAP = []
        for i in range(minLen):
            MAP.append(minValue[0:i + 1])

        count = 0
        mapLen = len(MAP)
        for i in range(mapLen):
            target = MAP[i]
            for j in range(length):
                if strs[j][0:i + 1] != target:
                    if count > 0:
                        return MAP[i - 1]
                    else:
                        return ""
            count += 1

        return MAP[mapLen - 1]


solution = Solution()
a = ["flower", "flow", "flight"]
# a = ["dog", "racecar", "car"]
# a = ["", ""]
print(solution.longestCommonPrefix(a))
