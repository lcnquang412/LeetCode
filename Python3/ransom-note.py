class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMapRansomNote = {}
        hashMapMagazine = {}
        for char in ransomNote:
            if char in magazine:
                if char not in hashMapRansomNote:
                    hashMapRansomNote[char] = 1
                else:
                    hashMapRansomNote[char] += 1
            else:
                return False

        for char in magazine:
            if char not in hashMapMagazine:
                hashMapMagazine[char] = 1
            else:
                hashMapMagazine[char] += 1

        for char in hashMapRansomNote:
            if char in hashMapMagazine:
                if hashMapRansomNote[char] > hashMapMagazine[char]:
                    return False
            else:
                return False
        return True


a = "aa"
b = "aab"
a = "aa"
b = "ab"
solution = Solution()
print(solution.canConstruct(a, b))
