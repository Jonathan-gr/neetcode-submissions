class Solution:
    def isValid(self, s: str) -> bool:
        

        parentheses = {')':'(',']':'[','}':'{'}
        stack = []
        for c in s:

            if c not in parentheses:
                stack.append(c)
                continue

            if len(stack)<=0:
                return False
            
            if stack.pop() != parentheses[c]:
                return False

        return len(stack)==0 
            


