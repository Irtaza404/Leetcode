class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        elif len(needle)==len(haystack):
            if needle==haystack:
                return 0
            return -1
        for i,s in enumerate(haystack):
            if i>len(haystack)-len(needle):
                return -1
            if s==needle[0]:
                if needle==haystack[i:i+len(needle)]:
                    return i
        return -1