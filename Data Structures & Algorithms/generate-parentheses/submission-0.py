class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        


        res,curr = [],[]
        def rec(l,r):
            if l==r==n:
                res.append("".join(curr.copy()))
                return
            
            if l<n:
                curr.append('(')
                rec(l+1,r)
                curr.pop()
            
            if r<l:
                curr.append(')')
                rec(l,r+1)
                curr.pop()
        
        rec(0,0)
        return res
