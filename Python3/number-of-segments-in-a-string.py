class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == 0:
            return 0
        result = 0
        isInSegment = False
        for char in s:
            if char == " ":
                if isInSegment:
                    isInSegment = False
            else:
                if not isInSegment:
                    result += 1
                    isInSegment = True
        return result


a = "Hello, my name is John"
a = "Hello"
a = "                "
solution = Solution()
print(solution.countSegments(a))
