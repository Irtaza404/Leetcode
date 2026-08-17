class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)-1):
                l,r=j+1,len(nums)-1
                while l<r:
                    total=nums[i]+nums[j]+nums[l]+nums[r]
                    if total==target:
                        t=[nums[i],nums[j],nums[l],nums[r]]
                        if t not in res:
                            res.append(t)
                    
                    if total<target:
                        l+=1
                    else:
                        r-=1
        return res