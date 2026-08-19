class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(b,o,c):
            if len(b)==2*n:
                res.append(b)
                return
            if o<n:
                backtrack(b+"(",o+1,c)
            if c<o:
                backtrack(b+")",o,c+1)
        res=[]
        backtrack("",0,0)
        return res