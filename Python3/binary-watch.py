class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        hourArray = [
            0,
            1,
            1,
            2,
            1,
            2,
            2,
            3,
            1,
            2,
            2,
            3,
        ]
        minuteArray = [
            0,
            1,
            1,
            2,
            1,
            2,
            2,
            3,
            1,
            2,
            2,
            3,
            2,
            3,
            3,
            4,
            1,
            2,
            2,
            3,
            2,
            3,
            3,
            4,
            2,
            3,
            3,
            4,
            3,
            4,
            4,
            5,
            1,
            2,
            2,
            3,
            2,
            3,
            3,
            4,
            2,
            3,
            3,
            4,
            3,
            4,
            4,
            5,
            2,
            3,
            3,
            4,
            3,
            4,
            4,
            5,
            3,
            4,
            4,
            5,
        ]
        result = []

        def buildTime(hour, minute):
            finalMinute = minute if minute > 9 else f'0{minute}'
            return f'{hour}:{finalMinute}'

        for i in range(12):
            for j in range(60):
                if hourArray[i] + minuteArray[j] == turnedOn:
                    result.append(buildTime(i, j))
        return result


a = 1
solution = Solution()
print(solution.readBinaryWatch(a))
print(bin(59).count("1"))
