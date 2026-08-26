class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=""
        for w in s.lower():
            if w.isalnum():
                r+=w
        print(r)
        if r==r[::-1]:
            return True
        return False