class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        
        l = 0
        r = 1
        maxP = 0

        while(r < len(prices)):
            # Sell the stock
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)

            else:
                # "Buy" the next cheaper stock
                l = r
            
            r += 1
        
        return maxP
