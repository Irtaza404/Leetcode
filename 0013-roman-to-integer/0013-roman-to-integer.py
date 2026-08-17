class Solution:
    def romanToInt(self, s: str) -> int:
        values={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        result=0
        prev = 0
        for val in s[::-1]:
            curr = values[val]
            if curr < prev:
                result -= curr
            else:
                result += curr
            prev = curr
        return result