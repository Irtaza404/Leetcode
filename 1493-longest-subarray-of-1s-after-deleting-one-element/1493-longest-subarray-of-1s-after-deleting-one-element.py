class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len=0
        count=l=0
        for r in range(len(nums)):
            if nums[r]!=1:
                count+=1
            while count>1:
                if nums[l]!=1:
                    count-=1
                l+=1
                
            max_len=max(max_len,r-l)
        
        return max_len