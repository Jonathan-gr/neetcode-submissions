class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        


        res,curr = [],[]

        def rec(i,total):
            if i>=len(nums) or total>target:
                return
            if total==target:
                res.append(curr.copy())
                return
            

            curr.append(nums[i])
            rec(i,total+nums[i])
            curr.pop()
            rec(i+1,total)
        rec(0,0)
        return res