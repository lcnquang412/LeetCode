class Solution:
    def __init__(self):
        self.CONVERTER = {
            1: {
                1: "I",
                5: "V",
                10: "X"
            },
            10: {
                1: "X",
                5: "L",
                10: "C"
            },
            100: {
                1: "C",
                5: "D",
                10: "M"
            }
        }

    def intToRoman(self, num: int) -> str:
        step = 1000
        result = ""
        while step > 0:
            div = int(num / step)
            if div > 0:
                if step == 1000:
                    for i in range(div):
                        result += "M"
                else:
                    converter = self.CONVERTER[step]
                    one = converter[1]
                    five = converter[5]
                    ten = converter[10]

                    if div == 4:
                        result += one + five
                    elif div == 9:
                        result += one + ten
                    elif div in converter:
                        result += converter[div]
                    elif div <= 3:
                        for _ in range(div):
                            result += one
                    elif div <= 8:
                        result += five
                        for _ in range(div - 5):
                            result += one
            num -= div * step
            step = int(step / 10)
        return result


a = 3749
a = 58
a = 1994
solution = Solution()
print(solution.intToRoman(a))
