class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimString = s.strip()
        arrString = trimString.split()
        return len(arrString[len(arrString) - 1])


solution = Solution()
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
