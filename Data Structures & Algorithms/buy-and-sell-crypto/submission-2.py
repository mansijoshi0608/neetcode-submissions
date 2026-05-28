class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_stock=1000
        for num in prices:
            min_stock=min(num,min_stock)
            max_profit=max(num-min_stock,max_profit)
        return max_profit


        