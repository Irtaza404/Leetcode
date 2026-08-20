from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len=0
        count={}
        l=0
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]]+=1
            else:
                count[s[r]]=1
            max_freq=max(count.values())
            while (r-l+1)-max_freq>k:
                count[s[l]]-=1
                l+=1
                max_freq=max(count.values())
            max_len=max(max_len,r-l+1)
        return max_len