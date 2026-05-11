class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        sety = set(nums)
        maxi = 0
        for n in nums:

            curr=1
            if n-1 not in sety:
                temp=n+1
                while temp in sety:
                    curr+=1
                    temp+=1
                maxi=max(maxi,curr)
        return maxi
