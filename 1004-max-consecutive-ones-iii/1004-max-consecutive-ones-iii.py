class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zero=0
        one=l=0
        for r in range(len(nums)):
            if nums[r]==0:
                zero+=1

            while zero>k:
                if nums[l]==0:
                    zero-=1
                l+=1
            one=max(one,r-l+1)
        return one
             