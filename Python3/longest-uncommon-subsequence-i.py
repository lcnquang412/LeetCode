class Solution:

    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))


a = 'aba'
b = 'cdc'
# a = 'aaa'
# b = 'bbb'
a = 'aaa'
b = 'aaa'
# a = 'aaa'
# b = 'aabb'
# a = "aefawfawfawfaw"
# b = "aefawfeawfwafwaef"
a = "aweffwaf"
b = "aweffwaf"
solution = Solution()
print(solution.findLUSlength(a, b))
