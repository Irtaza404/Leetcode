from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t=Counter(t)
        need=len(count_t)
        have=0
        window={}
        l=0
        min_len=float("inf")
        best_l=best_r=-1
        for r in range(len(s)):
            if s[r] in window:
                window[s[r]]+=1
            else:
                window[s[r]]=1
            
            if s[r] in count_t and window[s[r]]==count_t[s[r]]:
                have+=1
            
            while have==need:
                current=r-l+1
                if current < min_len:
                    min_len=current
                    best_r=r
                    best_l=l

                window[s[l]]-=1
                
                if s[l] in count_t and window[s[l]]<count_t[s[l]]:
                    have-=1
                l+=1
        return "" if min_len==float("inf") else s[best_l:best_r+1]