class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum=windowstart=size=0

        n=len(nums)
        min_len=n+1
        for i in range(n):
            window_sum+=nums[i]
            size+=1
            if window_sum>=target:
                while window_sum>=target:
                    window_sum-=nums[windowstart]
                    windowstart+=1
                    size-=1
                min_len=min(min_len,size+1)

        return min_len if min_len!=n+1 else 0


