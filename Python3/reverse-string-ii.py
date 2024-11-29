class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left = 0
        right = 0
        length = len(s)
        result = ''
        while right < length:
            right = left + 2 * k
            if right > length:
                right = length
            candidate2K = s[left:right]
            candidateKLeft = candidate2K[0:k]
            candidateKRight = candidate2K[k:right]
            if len(candidate2K) < k:
                candidateKLeft = candidate2K[0:len(candidate2K)]
                candidateKRight = candidate2K[len(candidate2K):right]
            left = right
            result += f'{candidateKLeft[::-1]}{candidateKRight}'
        return result


a = 'abcdefgh'
b = 3
solution = Solution()
print(solution.reverseStr(a, b))
