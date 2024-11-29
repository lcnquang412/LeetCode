class Solution:
    def __init__(self):
        self.hashMapRevert = {
            '0': 'f',
            '1': 'e',
            '2': 'd',
            '3': 'c',
            '4': 'b',
            '5': 'a',
            '6': '9',
            '7': '8',
            '8': '7',
            '9': '6',
            'a': '5',
            'b': '4',
            'c': '3',
            'd': '2',
            'e': '1',
            'f': '0',
        }
        self.listHex = [
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            'a',
            'b',
            'c',
            'd',
            'e',
            'f'
        ]

    def complement(self, hexStr: str):
        result = ''
        if len(hexStr) < 8:
            for i in range(8 - len(hexStr)):
                hexStr = '0' + hexStr
        for char in hexStr:
            result += self.hashMapRevert[char]
        return result

    def plusOne(self, hexStr):
        remain = 1
        length = len(hexStr)
        for i in range(length):
            if remain == 0:
                return hexStr
            else:
                lengthRevert = length - 1 - i
                element = hexStr[lengthRevert]
                indexElement = self.listHex.index(element)
                if indexElement + 1 > 15:
                    hexStr[lengthRevert] = '0'
                else:
                    hexStr[lengthRevert] = self.listHex[indexElement + 1]
                    remain = 0

        return hexStr if remain == 0 else hexStr.insert(0, '1')

    def removeZerosPrefix(self, hexStr):
        index = 0
        for char in hexStr:
            if char == '0':
                index += 1
            else:
                break
        return hexStr[index: len(hexStr)]

    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        elif num > 0:
            return hex(num).lstrip("0x")
        else:
            hexNum = hex(abs(num)).lstrip("0x")
            # print(hexNum)
            hexNumComplemented = self.complement(hexNum)
            # print(hexNumComplemented)
            hexNumRevertPlussedOne = self.plusOne(list(hexNumComplemented))
            return self.removeZerosPrefix(''.join(hexNumRevertPlussedOne))


a = -2147483648
solution = Solution()
print(solution.toHex(a))

# for i in range(16):
#     print(f'\'{hex(i).lstrip("0x")}\': \'{hex(15 - i).lstrip("0x")}\',')

# for i in range(16):
#     print(f'\'{hex(i).lstrip("0x")}\'')
