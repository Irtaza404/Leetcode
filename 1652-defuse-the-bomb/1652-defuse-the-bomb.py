class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        
        if k == 0:
            return [0] * n
            
        code += code
        res = []
        
        if k > 0:
            start = 1
            s = 0
            r = 1
            
            while len(res) < n:
                s += code[r]
                
                if r - start + 1 == k:
                    res.append(s)
                    s -= code[start]
                    start += 1
                
                r += 1
                
        elif k < 0:
            k_abs = abs(k)
            start = n - k_abs
            s = 0
            r = start
            
            while len(res) < n:
                s += code[r]
                
                if r - start + 1 == k_abs:
                    res.append(s)
                    s -= code[start]
                    start += 1
                    
                r += 1
                
        return res