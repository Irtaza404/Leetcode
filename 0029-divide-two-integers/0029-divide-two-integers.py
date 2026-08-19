class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # handle overflow edge case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # determine sign
        negative = (dividend < 0) != (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
    
        while dividend>=divisor:
            t=divisor
            m=1
            while dividend>=(t<<1):
                t<<=1
                m<<=1
            dividend-=t
            quotient+=m
        
        return -quotient if negative else quotient