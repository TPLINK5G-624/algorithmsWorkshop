class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i,j = len(matrix)-1,0
        while i>=0 and j>=0 and i<len(matrix) and j<len(matrix[i]):
            #print(matrix[i][j])
            if matrix[i][j] == target :
                return True
            if matrix[i-1][j] >= target:
                i-=1
            else:
                j+=1
        return False
            