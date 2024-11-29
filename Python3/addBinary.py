class Solution:
    def __init__(self):
        self.remember = 0

    def addBinary(self, a: str, b: str) -> str:
        min = a
        max = b

        def add(c1: str, c2: str):
            tmp = 2 * self.remember + 2 * int(c1) + 2 * int(c2)
            if tmp == 0 or tmp == 2:
                self.remember = 0
            else:
                self.remember = 1
            if tmp == 0 or tmp == 4:
                return "0"
            else:
                return "1"

        if len(a) > len(b):
            min = b
            max = a
        min = list(min)
        max = list(max)
        minLength = len(min)
        maxLength = len(max)
        for i in range(maxLength):
            # print(f'{max} {self.remember}')
            minIndex = minLength - 1 - i
            maxIndex = maxLength - 1 - i

            if minIndex < 0:
                max[maxIndex] = add(max[maxIndex], "0")
            else:
                max[maxIndex] = add(max[maxIndex], min[minIndex])

        if self.remember == 1:
            max.insert(0, "1")

        return ''.join(max)


a = "1111"
b = "1111"
# a = "11"
# b = "1"
solution = Solution()
print(solution.addBinary(a, b))
