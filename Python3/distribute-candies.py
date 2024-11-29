class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        return min(int(len(candyType) / 2), len(set(candyType)))


a = [1, 1, 2, 2, 3, 3]
# a = [1, 1, 2, 3]
# a = [6, 6, 6, 6]
solution = Solution()
print(solution.distributeCandies(a))

# Slow
#     hashMapPositive = [0] * 100000
#         hashMapNegative = [0] * 100000
#         countType = 0
#         halfCandyType = int(len(candyType) / 2)
#         for t in candyType:
#             if t >= 0:
#                 if hashMapPositive[t] == 0:
#                     countType += 1
#                 hashMapPositive[t] += 1
#             else:
#                 if hashMapNegative[abs(t)] == 0:
#                     countType += 1
#                 hashMapNegative[abs(t)] += 1
#         return countType if halfCandyType > countType else halfCandyType
