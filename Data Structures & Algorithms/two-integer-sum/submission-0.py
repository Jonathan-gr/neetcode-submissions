class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        placements = {}

        for i,n in enumerate(nums):
            temp = target - n
            if temp in placements:
                return [placements[temp],i]
            
            placements[n] = i