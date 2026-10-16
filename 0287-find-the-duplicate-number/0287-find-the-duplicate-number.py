class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f,s=nums[nums[0]],nums[0]
        while s!=f:
            f=nums[nums[f]]
            s=nums[s]
        s=0
        while s!=f:
            f=nums[f]
            s=nums[s]

        return s