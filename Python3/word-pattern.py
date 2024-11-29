class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sArr = s.split(' ')
        i = 0
        hashMap = {}
        cache = {}
        if len(sArr) != len(pattern):
            return False
        for pChar in pattern:
            sChar = sArr[i]
            if pChar not in hashMap:
                if sChar in cache:
                    return False
                else:
                    cache[sChar] = True
                hashMap[pChar] = sChar
            else:
                if hashMap[pChar] != sChar:
                    return False
            i += 1
        return True


a = "abba"
b = "dog cat cat dog"
a = "abba"
b = "dog cat cat fish"
a = "aaaa"
b = "dog cat cat dog"
a = "abba"
b = "dog dog dog dog"
solution = Solution()
print(solution.wordPattern(a, b))
