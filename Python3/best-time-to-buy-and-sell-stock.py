class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        result = 0
        minBuy = prices[0]
        for i in range(1, len(prices)):
            result = max(result, prices[i] - minBuy)
            minBuy = min(minBuy, prices[i])
        return result


a = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maxProfit(a))
