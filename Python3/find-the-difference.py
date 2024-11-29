class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashMapS = {}
        hashMapT = {}
        for char in s:
            hashMapS[char] = 1 if char not in hashMapS else hashMapS[char] + 1
        for char in t:
            hashMapT[char] = 1 if char not in hashMapT else hashMapT[char] + 1
        for char in hashMapT:
            if char not in hashMapS:
                return char
            else:
                if hashMapS[char] < hashMapT[char]:
                    return char
        return None


a = "abcd"
b = "abcde"
solution = Solution()
print(solution.findTheDifference(a, b))
