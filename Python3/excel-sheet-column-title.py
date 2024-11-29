import math


class Solution:
    def __init__(self):
        self.ALPHABET = ["A",
                         "B",
                         "C",
                         "D",
                         "E",
                         "F",
                         "G",
                         "H",
                         "I",
                         "J",
                         "K",
                         "L",
                         "M",
                         "N",
                         "O",
                         "P",
                         "Q",
                         "R",
                         "S",
                         "T",
                         "U",
                         "V",
                         "W",
                         "X",
                         "Y",
                         "Z"]

    def convertToTitle(self, columnNumber: int) -> str:
        # print(columnNumber)
        if columnNumber <= 26:
            return self.ALPHABET[columnNumber - 1]
        mod = columnNumber % 26
        div = columnNumber / 26
        if mod == 0:
            div = columnNumber / 26 - 1

        return f'{self.convertToTitle(math.floor(div))}{self.convertToTitle(mod)}'


solution = Solution()
a = 701
# a = 52
print(solution.convertToTitle(a))
