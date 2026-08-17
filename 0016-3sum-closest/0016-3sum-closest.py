class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closest_sum=10**5
        for i in range(n):
            l,r=i+1,n-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                if target==closest_sum:
                    return closest_sum
                elif total<target:
                    l+=1
                else:
                    r-=1 
        return closest_sum