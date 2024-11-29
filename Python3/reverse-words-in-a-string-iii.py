class Solution:
    def reverseWords(self, s: str) -> str:
        sArr = s.split(" ")
        for i in range(len(sArr)):
            sArr[i] = sArr[i][::-1]
        return " ".join(sArr)


a = "Let's take LeetCode contest"
solution = Solution()
print(solution.reverseWords(a))
