import sys
class Solution(object):
    def maxProfit(self, prices):
        l,r = 0,1
        P = 0
        while r<len(prices):
            if prices[l]<prices[r]:
                Profit = prices[r] - prices[l]
                P = max(P, Profit)
            else:
                l = r
            r += 1
        return P

        