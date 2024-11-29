class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = ''
        number = ''
        for char in s:
            if char == '-' or char == '+':
                if sign == '':
                    sign = char
                else:
                    break
            elif '0' <= char <= '9':
                if sign == '':
                    sign = '+'
                number += char
            else:
                break
        if number == '':
            return 0
        else:
            result = int(number)
            result = result * (-1 if sign == '-' else 1)
            result = -2 ** 31 if result < -2 ** 31 else result
            result = 2 ** 31 - 1 if result > 2 ** 31 - 1 else result
            return result


a = '42'
a = ' -042'
a = '1337c0d3'
a = '0-1'
a = '-91283472332'
solution = Solution()
print(solution.myAtoi(a))
