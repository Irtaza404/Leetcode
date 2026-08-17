class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i,n in enumerate(nums):
            sub=target-n
            if n in seen:
                return [seen[n],i]
            else:
                seen[sub]=i