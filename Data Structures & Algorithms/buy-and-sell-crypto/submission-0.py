class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        n=len(prices)
        buy=prices[0]
        for i in range(1,n,1):
            if prices[i]>buy:
                max_profit=max(prices[i]-buy,max_profit)
            else:
                buy=prices[i]
        return max_profit
        