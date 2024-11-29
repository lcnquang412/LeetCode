class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        indexG = 0
        indexS = 0
        g.sort()
        s.sort()

        while indexS < len(s) and indexG < len(g):
            if s[indexS] >= g[indexG]:
                indexG += 1
            indexS += 1
            if indexS == len(s) or indexG == len(g):
                return indexG
        return indexG


a = [1, 2, 3]
b = [1, 1]
# a = [1, 2]
# b = [1, 2, 3]
solution = Solution()
print(solution.findContentChildren(a, b))
