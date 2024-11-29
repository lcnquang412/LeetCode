class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        result = ''
        maxResult = -1
        for char in s:
            if char not in result:
                result += char
            else:
                index = result.find(char)
                if index == len(result) - 1:
                    result = char
                else:
                    result = f'{result[index + 1:len(result)]}{char}'
            print(result)
            maxResult = max(maxResult, len(result))
        return maxResult


a = 'abcabcbb'
# a = 'bbbbb'
# a = 'pwwkew'
# a = 'aab'
# a = 'dvdf'
# a = ''
# a = 'aabaab!bb'
solution = Solution()
print(solution.lengthOfLongestSubstring(a))
