class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Max benefit from prices[i:]
        1) If we're buying at i, larger value of either
            a) buy at i, sell at i+1~
            b) do nothing at i, buy at i+1~
        2) If we're selling at i, larger value of either
            a) sell at i, buy at i+2~
            b) do nothing at i, sell at i+1~
        """

        buyings = [0] * len(prices)
        sellings = [0] * len(prices)

        for i in range(len(prices) - 1, -1, -1):
            buyings[i] = max(
                -prices[i] + (sellings[i + 1] if i + 1 < len(prices) else 0),
                buyings[i + 1] if i + 1 < len(prices) else 0
            )
            sellings[i] = max(
                prices[i] + (buyings[i + 2] if i + 2 < len(prices) else 0),
                sellings[i + 1] if i + 1 < len(prices) else 0
            )
        return buyings[0]

