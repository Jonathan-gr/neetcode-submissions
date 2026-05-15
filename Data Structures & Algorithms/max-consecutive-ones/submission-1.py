class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        

  
        curr_val = 0
        maxi = 0

        for n in nums:
            if n==1:
                curr_val+=1
            else:
                
                maxi = max(maxi,curr_val)
                curr_val = 0

            curr_num = n
                
        
        maxi = max(maxi,curr_val)
        return maxi