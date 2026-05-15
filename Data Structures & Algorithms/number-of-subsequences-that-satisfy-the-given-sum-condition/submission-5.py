class Solution:
    def numSubseq(self, nums: List[int], target: int):
        
        nums.sort()
        MOD = 10**9 + 7

        n = len(nums)
        r = n - 1
        res = 0

        # precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        for l in range(n):

            while r >= l and nums[l] + nums[r] > target:
                r -= 1

            if r >= l:
                res = (res + pow2[r - l]) % MOD

        return res