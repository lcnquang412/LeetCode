class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.find('LLL') > -1:
            return False
        count = 0
        for char in s:
            count += 1 if char == "A" else 0
            if count > 1:
                return False
        return True


a = "PPALLP"
a = "PPALLL"
solution = Solution()
print(solution.checkRecord(a))
