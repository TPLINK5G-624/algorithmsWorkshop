class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        di = {}
        res = []
        for i in nums:
            if i not in di:
                di[i] = 0
            else:
                di[i] += 1
        for k in di.keys():
            if di[k] > 0:
                res.append(k)
        return res[0]