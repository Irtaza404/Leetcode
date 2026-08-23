class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l=0
        data=""
        count=0
        for r in range(len(s)):
            data+=s[r]
            if r>=2:
                if len(set(data))==3:
                    count+=1
                data=data[1:]
                l+=1
        return count