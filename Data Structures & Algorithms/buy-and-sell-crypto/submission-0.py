class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window 
        # naive approach:
        max_profit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i, n): # O(n^2)
                curr = prices[j] - prices[i]
                if curr > max_profit:
                    max_profit = curr

        return max_profit