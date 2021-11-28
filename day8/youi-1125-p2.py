class Solution:
    def numWays(self, n: int) -> int:
        li = [1,1,2] + [None] * (n-2)
        for i in range(3,n+1):
            li[i]=(li[i-1]+li[i-2])%1000000007
        return li[n]