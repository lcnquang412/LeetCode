class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}
        cache = []
        for char in s:
            if char not in hashMap:
                hashMap[char] = True
                cache.append(char)
            elif char in cache:
                cache.remove(char)
        if cache:
            return s.find(cache[0])
        else:
            return -1


a = "leetcode"
# a = "loveleetcode"
solution = Solution()
print(solution.firstUniqChar(a))
