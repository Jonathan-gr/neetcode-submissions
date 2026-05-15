class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        

        nums.sort()

        r = len(nums)-1
        res = 0
        MOD = (10**9)+7


        for l in range(len(nums)):

            while (r>=l and nums[l]+nums[r]>target):
                r-=1
            if r>=l:
                res += pow(2, r - l, MOD)
                res %= MOD
        return res