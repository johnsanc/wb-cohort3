class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        daily_profit = [0 for x in range(len(prices) + 1)]
        daily_profit[0] = 0
        
        self.profit_helper(daily_profit, prices)
        return max(daily_profit)
    
    def profit_helper(self, arr, price_list):
        l_prices = len(price_list)
        if l_prices < 2:
            return
        elif l_prices == 2:
            if price_list[1] < price_list[0]:
                arr.append(0)
                return 
            else:
                arr.append(price_list[1] - price_list[0])
                return 
        else:
            
            day_profit = 0
            for i in range(l_prices - 1):
                if price_list[l_prices-1] - price_list[i] > 0:
                    day_profit = max(day_profit, price_list[l_prices-1] - price_list[i])
            arr.append(day_profit)
            self.profit_helper(arr, price_list[:l_prices-1])

# A recursive algorithm that did not pass the test cases that had large lists
# An example of my thought process while attempting a problem with no prior 
# knowledge, but the requirement being that it be recursive.  I would have 
# normally tried an iterative approach instead.