class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = [nums[0]] + [None] *(len(nums)-1)
        res = nums[0]
        for i in range(1,len(nums)):
            maxSum[i] = max(nums[i],nums[i]+maxSum[i-1])
            res = max(maxSum[i],res)
        return res