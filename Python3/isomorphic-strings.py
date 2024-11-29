class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = {}
        for i in range(len(s)):
            if s[i] not in hashMap:
                if t[i] in hashMap.values():
                    return False
                else:
                    hashMap[s[i]] = t[i]
            elif hashMap[s[i]] != t[i]:
                return False
        return True


a = "egg"
b = "add"
# a = "foo"
# b = "bar"
# a = "paper"
# b = "title"
# a = "badc"
# b = "baba"
solution = Solution()
print(solution.isIsomorphic(a, b))
