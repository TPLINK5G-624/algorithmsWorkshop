class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers)-1
        while l <= r:
            m = (l+r)//2
            if l == r:
                return numbers[l]
            if numbers[m] > numbers[r]:
                l = m + 1
            elif numbers[m] < numbers[r]:
                r = m
            elif numbers[m] == numbers[r]:
                r -= 1