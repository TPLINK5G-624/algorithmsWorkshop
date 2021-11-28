class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        maxMat = [[None] * n ] * m
        for mi in range(0,m):
            for ni in range(0,n):
                op_path = 0
                if mi > 0 and ni > 0:
                    op_path = max(maxMat[mi-1][ni], maxMat[mi][ni-1])
                elif mi > 0 and ni==0:
                    op_path =  maxMat[mi-1][ni]
                elif mi == 0 and ni > 0:
                    op_path =  maxMat[mi][ni-1]
                maxMat[mi][ni] = grid[mi][ni] + op_path 
        return maxMat[m-1][n-1]