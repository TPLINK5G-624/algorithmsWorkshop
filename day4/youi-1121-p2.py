class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        flag = 0
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                flag = 1 
                break
            elif nums[m] > target:
                r = m -1
            elif nums[m] < target:
                l = m + 1
        count = 0 
        if flag == 1 :
            while m > 0 and nums[m-1]== target:
                m -= 1
            while m <len(nums) and nums[m] == target:
                count += 1
                m += 1
        return count