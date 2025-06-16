import math

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        def getFreeLand(_countFreeLand: int, _boundaries: int) -> int:
            freeLand = countFreeLand - boundaries
            if freeLand > 0:
                return math.ceil(freeLand / 2)
            return 0

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        countFreeLand = 0
        maxFlowers = 0
        start = True
        for hasFlower in flowerbed:
            if hasFlower:
                boundaries = 2
                if start:
                    boundaries = 1
                    start = False
                maxFlowers += getFreeLand(countFreeLand, boundaries)
                countFreeLand = 0
            else:
                countFreeLand += 1

        if countFreeLand > 0:
            boundaries = 1
            if start:
                boundaries = 0
            maxFlowers += getFreeLand(countFreeLand, boundaries)

        return n <= maxFlowers


solution = Solution()
a = [0, 0, 0]
n = 2
print(solution.canPlaceFlowers(a, n))