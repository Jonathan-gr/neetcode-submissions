class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res,curr = [],[]
        def rec():

            if len(curr)==len(nums):
                res.append(curr.copy())
                return
            
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    rec()
                    curr.pop()
        rec()
        return res