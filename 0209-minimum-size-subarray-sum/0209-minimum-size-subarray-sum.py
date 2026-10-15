class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum=0
        size=float("inf")
        l=0
        for r in range(len(nums)):
            window_sum+=nums[r]

            while window_sum >= target:
                size=min(size,r-l+1)
                window_sum-=nums[l]
                l+=1
            
            

        return  size if size != float("inf") else 0

