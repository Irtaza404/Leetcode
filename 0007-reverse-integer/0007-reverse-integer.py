class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX,INT_MIN=2**31-1,-2**31
        num=0
        temp=x
        x=abs(x)
        while x!=0:
            last=x%10 
            x//=10 
            num=num*10+last 
        if temp<0:
            num=-num        
        if num > INT_MAX or num < INT_MIN:
            return 0
        return num
