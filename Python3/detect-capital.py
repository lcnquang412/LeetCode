class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        firstCharUpperCase = False
        secondCharUpperCase = False
        for i in range(len(word)):
            char = word[i]
            if i == 0:
                if 'A' <= char <= 'Z':
                    firstCharUpperCase = True
            elif i == 1:
                if firstCharUpperCase:
                    if 'A' <= char <= 'Z':
                        secondCharUpperCase = True
                else:
                    if 'A' <= char <= 'Z':
                        return False
            else:
                if firstCharUpperCase:
                    if secondCharUpperCase:
                        if 'a' <= char <= 'z':
                            return False
                    else:
                        if 'A' <= char <= 'Z':
                            return False
                else:
                    if 'A' <= char <= 'Z':
                        return False
        return True


a = "USA"
a = 'FlaG'
a = 'Leetcode'
a = "isA"
solution = Solution()
print(solution.detectCapitalUse(a))
