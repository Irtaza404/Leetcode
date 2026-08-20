class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        check=True
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                check=False
                break
        if check:
            nums.reverse()
        else:
            for j in range(len(nums)-1,-1,-1):
                if nums[j]>nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
                    break
            nums[i+1:] = reversed(nums[i+1:])
