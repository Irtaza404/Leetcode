class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap):
            day=1
            s=0
            for w in weights:
                if s+w>cap:
                    day+=1
                    s=w
                else:
                    s+=w
            return day<=days
            
        l,h=max(weights),sum(weights)
        least=0
        while l<=h:
            cap=(l+h)//2
            if can_ship(cap):
                least=cap
                h=cap-1
            else:
                l=cap+1
        return least 