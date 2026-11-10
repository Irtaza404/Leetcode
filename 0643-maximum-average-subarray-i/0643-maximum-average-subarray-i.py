class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=l=0
        maxavg=float("-inf")
        for r in range(len(nums)):
            window+=nums[r]
            if r>=k-1:
                maxavg=max(window/k,maxavg)
                window-=nums[l]
                l+=1
        return maxavg