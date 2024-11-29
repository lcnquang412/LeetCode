class Solution:

    def romanToInt(self, s: str) -> int:
        MAP = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        length = len(s)
        isContinue = False
        result = 0
        for i in range(length):
            if isContinue:
                isContinue = False
                continue

            if i + 2 <= length:
                ssElement = s[i:i + 2]
                if ssElement in MAP:
                    result += MAP[ssElement]
                    isContinue = True
                    continue

            eElement = s[i]
            if eElement in MAP:
                result += MAP[eElement]
                isContinue = False
        return result


solution = Solution()
print(solution.romanToInt('MCMXCIV'))
