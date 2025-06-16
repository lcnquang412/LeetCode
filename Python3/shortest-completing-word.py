class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        mapLicensePlate = {}
        licensePlate = licensePlate.lower()
        result = 'aaaaaaaaaaaaaaaa'

        def setToMap(_word, _map):
            for _char in _word:
                if "a" <= _char <= "z":
                    if _char in _map:
                        _map[_char] += 1
                    else:
                        _map[_char] = 1

        setToMap(licensePlate, mapLicensePlate)

        for word in words:
            mapWord = {}
            for char in word:
                if char in mapLicensePlate:
                    if char in mapWord:
                        mapWord[char] += 1
                    else:
                        mapWord[char] = 1

            isFound = True
            for char in mapLicensePlate:
                if not (char in mapWord and mapWord[char] >= mapLicensePlate[char]):
                    isFound = False
                    break

            if isFound and len(word) < len(result):
                result = word

        return result


# a = "1s3 PSt"
# b = ["step", "steps", "stripe", "stepple"]
a = "1s3 456"
b = ["looks", "pest", "stew", "show"]
solution = Solution()
print(solution.shortestCompletingWord(a, b))
