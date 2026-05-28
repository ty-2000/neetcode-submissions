class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Instead of keep max_profit in global, retun the profit from the function at this point
        # If we can buy a coin:
        # # 1) Buy, Can sell after any time
        # # 2) Do nothing. Buy after any time

        # If not (eligible to sell)
        # # 1) Sell, Can buy any time 2 days after
        # # 2) Do nothing. Sell after any time

        memo = {}
        def dfs(i: int, buying: bool):
            if (i, buying) in memo:
                return memo[(i, buying)]
            if i >= len(prices):
                return 0
            
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, False) - prices[i]
                memo[(i, buying)] = max(cooldown, buy)
                return memo[(i, buying)]
            else:
                sell = dfs(i + 2, True) + prices[i]
                memo[(i, buying)] = max(cooldown, sell)
                return memo[(i, buying)]
        return dfs(0, True)
