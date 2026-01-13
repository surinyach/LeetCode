class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_val = prices[0]
        for i in range(1, len(prices)):
            p = prices[i]
            if p > min_val:
                profit += p - min_val
                min_val = p
            else:
                min_val = p
            
        return profit