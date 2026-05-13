class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        max_pos,max_neg = 1,1
        res = -float('inf')
        for n in nums:

            temp = max_pos
            max_pos = max(n,max_pos*n,max_neg*n)
            max_neg = min(n,temp*n,max_neg*n)
            res = max(res,max_pos)
        
        return res