class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        minLetter = "{"
        for letter in letters:
            if target < letter < minLetter:
                minLetter = letter
        return minLetter if minLetter != "{" else letters[0]


a = ["c", "f", "j"]
b = "a"
a = ["c", "f", "j"]
b = "c"
a = ["x", "x", "y", "y"]
b = "z"
solution = Solution()
print(solution.nextGreatestLetter(a, b))
