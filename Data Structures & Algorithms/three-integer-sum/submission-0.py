class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []
        skip = None
        for i in range(len(nums)-2):
            if nums[i]==skip:
                continue
            l,r = i+1,len(nums)-1

            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    res.append([nums[i],nums[l],nums[r]])
                    skip = nums[i]
                    temp = nums[l]
                    while l<r and temp==nums[l]:
                        l+=1
                
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    r-=1
        return res






