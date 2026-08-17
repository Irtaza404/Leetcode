class Solution:
    def isValid(self, ss: str) -> bool:
        stack=[]
        for s in ss:
            if stack==[] or s =="{" or s=="[" or s=="(":
                stack.append(s)
            elif (stack[-1]=="(" and s==")") or (stack[-1]=="{" and s=="}") or(stack[-1]=="[" and s=="]")  :
                stack.pop()
            else:
                return False
        return False if stack else True 