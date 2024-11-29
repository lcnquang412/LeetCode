class Solution:
    def climbStairs(self, n: int) -> int:
        mapping = [1, 2, 3]
        if n <= len(mapping):
            return mapping[n - 1]
        else:
            for i in range(3, n):
                mapping.append(mapping[i - 1] + mapping[i - 2])
            return mapping.pop()
        return 0


solution = Solution()
print(solution.climbStairs(45))

# Original
# mapping = [1, 2, 3]
# if n <= len(mapping):
#     return mapping[n - 1]
# else:
#     for i in range(3, n):
#         mapping.append(mapping[i - 1] + mapping[i - 2])
#     return mapping.pop()

# Cheat
# mapping = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
#                    28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887,
#                    9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437,
#                    701408733, 1134903170, 1836311903]
# return mapping[n - 1]
