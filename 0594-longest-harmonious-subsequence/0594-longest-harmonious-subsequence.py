from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count=Counter(nums)
        maxl=0
        for x in count:
            if x+1 in count:
                maxl=max(maxl,count[x]+count[x+1])
        return maxl