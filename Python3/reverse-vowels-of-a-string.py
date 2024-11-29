import math


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowelIndex = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowelIndex.append(i)

        sArray = list(s)
        for index in range(math.floor(len(vowelIndex) / 2)):
            i = vowelIndex[index]
            j = vowelIndex[len(vowelIndex) - 1 - index]
            tmp = sArray[i]
            sArray[i] = sArray[j]
            sArray[j] = tmp
        return "".join(sArray)


a = 'IceCreAm'
a = 'leetcode'
solution = Solution()
print(solution.reverseVowels(a))
