class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=l=0
        max_avg=float("-inf")
        for r in range(len(nums)):
            window+=nums[r]
            if r>=k-1:
                max_avg=max(max_avg,window/k)
                window-=nums[l]
                l+=1
        return max_avg