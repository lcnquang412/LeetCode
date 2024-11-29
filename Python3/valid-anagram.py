class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sHashMap = {}
        tHashMap = {}
        for i in range(len(s)):
            if s[i] in sHashMap:
                sHashMap[s[i]] += 1
            else:
                sHashMap[s[i]] = 0
            if t[i] in tHashMap:
                tHashMap[t[i]] += 1
            else:
                tHashMap[t[i]] = 0
        for key in sHashMap.keys():
            if key not in tHashMap or sHashMap[key] != tHashMap[key]:
                return False
        return True


a = "anagram"
b = "nagaram"
# a = "rat"
# b = "car"
solution = Solution()
print(solution.isAnagram(a, b))

# Sort
#         sList = sorted(s)
#         tList = sorted(t)
#         for i in range(len(sList)):
#             if sList[i] != tList[i]:
#                 return False
#         return True
