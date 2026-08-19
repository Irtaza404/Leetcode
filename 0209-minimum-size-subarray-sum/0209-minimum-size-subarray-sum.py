class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        window_start = 0
        n = len(nums)
        min_len = n + 1
        
        for i in range(n):
            window_sum += nums[i]
            
            # We don't need the 'if', we can just use the 'while'!
            while window_sum >= target:
                # 1. Record the size BEFORE we shrink it
                min_len = min(min_len, i - window_start + 1)
                
                # 2. Shrink it
                window_sum -= nums[window_start]
                window_start += 1

        return min_len if min_len != n + 1 else 0