from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        freq=Counter(p)
        res=[]
        l=0
        word=Counter()
        for r in range(len(s)):
            word[s[r]]+=1 
            if r>=len(p)-1:
                if word==freq:
                    res.append(l)
                word[s[l]]-=1
                
                if word[s[l]]==0:
                    del word[s[l]]
                
                l+=1

        return res
        