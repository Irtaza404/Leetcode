class Solution:
    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float:
        # num=sorted(nums1+nums2)
        # l=len(num)
        # if l%2==0:
        #     l//=2
        #     return (num[l-1]+num[l])/2
        # else:
        #     return num[l//2]

        if len(n1)>len(n2):
            n1,n2=n2,n1
        
        m,n=len(n1),len(n2)
        total=m+n
        half=(total +1 )//2
        lo,hi=0,m
        while lo<=hi:
            i=(lo+hi)//2
            j=half-i

            l1=n1[i-1] if i>0 else float("-inf")
            r1=n1[i] if i<m else float("inf")
            l2=n2[j-1] if j>0 else float("-inf")
            r2=n2[j] if j<n else float("inf")

            if l1<=r2 and l2<=r1:
                if total%2==1:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
            elif l1>r2:
                hi=i-1
            else:
                lo=i+1