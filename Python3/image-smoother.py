import math


class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        rLength = len(img)
        cLength = len(img[0])
        result: list[list[int]] = [[0 for _i in range(cLength)] for _j in range(rLength)]
        rTemplate: list[int] = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        cTemplate: list[int] = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

        def count(r, c):
            divisionBy = 0
            for _i in range(len(rTemplate)):
                rNew = r + rTemplate[_i]
                cNew = c + cTemplate[_i]
                if 0 <= rNew < rLength and 0 <= cNew < cLength:
                    result[r][c] += img[rNew][cNew]
                    divisionBy += 1

            result[r][c] = math.floor(result[r][c] / divisionBy)

        for i in range(rLength):
            for j in range(cLength):
                count(i, j)

        return result


# a = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
# a = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]
a = [[1]]
solution = Solution()
print(solution.imageSmoother(a))
