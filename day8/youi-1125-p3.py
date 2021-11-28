class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        P = [0]+[None]*len(prices)
        t = 0
        m = 0
        for i in range(1,len(prices)):
            P[i] = prices[i]-prices[t]
            m = P[i] if P[i]> m else m
            if P[i] < 0:
                t = i  
                i += 1
            #print(t)
        return m