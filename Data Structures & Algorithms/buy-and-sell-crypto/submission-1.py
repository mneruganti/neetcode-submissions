class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0 # left = buy
        maxProfit = 0

        for r in range(1, len(prices)): # right = sell
            if prices[l] < prices[r]: # we want to sell when it is higher than buy
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else:
                l = r # if right < less, we want l to be the lower one?
            r += 1
        return maxProfit

             
            
        