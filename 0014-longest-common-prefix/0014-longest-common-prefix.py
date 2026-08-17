class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first, *r = sorted(strs, key=len)
        res = ""
        for c in first:
            avl = True
            for word in r:
                if word.startswith(res + c):
                    continue
                else:
                    avl = False
                    break
            if avl:
                res += c
            else:
                break

        return res
        