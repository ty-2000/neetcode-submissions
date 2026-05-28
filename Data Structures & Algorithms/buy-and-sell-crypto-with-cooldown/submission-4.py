class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Max benefit of prices[i:] is
        # 1) Max benefit of prices[i + 1:] OR # Do nothing at i
        # 2) For every j > i, max(prices[j] - prices[i] + max benefit of prices[j + 2:]) # Buy at i, cell at j
        # DP
        
        dp = [0] * len(prices) # Keep the max benefit from prices[i:]
        for i in range(len(prices) - 2, -1, -1):
            max_p = dp[i + 1]
            for j in range(i + 1, len(prices)):
                max_p = max(
                    prices[j] - prices[i] + (dp[j + 2] if j + 2 < len(prices) else 0),
                    max_p
                )
            dp[i] = max_p
        return dp[0]
