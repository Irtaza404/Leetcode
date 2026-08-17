class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reverse=0
        temp=x
        while temp!=0:
            n=temp%10
            temp//=10
            reverse=reverse*10+n
        if x==reverse:
            return True
        else:
            return False