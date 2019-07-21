class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        length = len(prices)
        memo = [0 for x in range(length)]
        lower_price = prices[0]
        
        for i in range(1, length):
            memo[i] = max(memo[i-1], prices[i] - lower_price)
            lower_price = min(lower_price, prices[i])
            
        return memo[length-1]