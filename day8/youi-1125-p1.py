class Solution:
    def fib(self, n: int) -> int:
        l = [0,1]
        for i in range(0,n+1):
            if i < 2:
                continue
            l.append( (l[i-1]+l[i-2])%(1000000007) )
        return l[n]