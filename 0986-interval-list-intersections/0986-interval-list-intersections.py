class Solution:
    def intervalIntersection(self, firstlist: List[List[int]], secondlist: List[List[int]]) -> List[List[int]]:
        res=[]
        p1=p2=0
        while p1<len(firstlist) and p2<len(secondlist):
            start1,end1=firstlist[p1]
            start2,end2=secondlist[p2]
            overlap_start=max(start1,start2)
            overlap_end=min(end1,end2)
            if overlap_start<=overlap_end:
                res.append([overlap_start,overlap_end])
            if end1<end2:
                p1+=1
            else:
                p2+=1

        return res