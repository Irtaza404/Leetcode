import math
class Solution:
    def minEatingSpeed(self, piles: List[int], ho: int) -> int:
        def can_finished(speed):
            hours=0
            for p in piles:
                hours += math.ceil(p / speed) 
            return hours<=ho
        
        l,h=1,max(piles)
        k=0
        while l<=h:
            mid=(l+h)//2
            if can_finished(mid):
                k=mid
                h=mid-1
            else:
                l=mid+1
        return k