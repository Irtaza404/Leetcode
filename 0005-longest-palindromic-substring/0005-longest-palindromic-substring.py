class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        result = ""
        for i in range(len(s)):
            odd = expand(s, i, i)
            even = expand(s, i, i+1)
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        return result
        
        # m = ""
        # for i in [s[i:j] for i in range(len(s)) for j in range(i, len(s)+1)]:
        #     if i == i[::-1]:
        #         if len(m) < len(i):
        #             m = i
        # return m
        
