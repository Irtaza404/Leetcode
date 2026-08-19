class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg=float("-inf")
        window_sum=window_start=0
        for i in range (len(nums)):
            window_sum+=nums[i]
            if i>=k-1:
                max_avg=max(max_avg,window_sum)
                window_sum-=nums[window_start]
                window_start+=1
        return max_avg/k