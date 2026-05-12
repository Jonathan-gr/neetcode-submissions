class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        res = []
        curr = []

        def rec(i):

            if i>=len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            rec(i+1)
            curr.pop()
            rec(i+1)
        rec(0)
        return res