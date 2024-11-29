class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        keyboard = [
            'qwertyuiop',
            'asdfghjkl',
            'zxcvbnm'
        ]
        result = []

        for word in words:
            for wordInKeyboardLine in keyboard:
                count = 0
                for char in word.lower():
                    if char not in wordInKeyboardLine:
                        break
                    else:
                        count += 1
                if count == len(word):
                    result.append(word)
                    continue
        return result


a = ["Hello", "Alaska", "Dad", "Peace"]
solution = Solution()
print(solution.findWords(a))
