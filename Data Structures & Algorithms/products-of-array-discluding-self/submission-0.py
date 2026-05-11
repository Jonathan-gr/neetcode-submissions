class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        going_left = [1]
        temp=1
        for i in range(len(nums)-1):
            temp*=nums[i]
            going_left.append(temp)
        
        going_right = [1]*len(nums)

        temp = 1
        for i in reversed(range(1,len(nums))):
            temp*=nums[i]
            going_right[i-1]=temp
        
        
     
        for i in range(len(nums)):
            going_right[i]*=going_left[i]
        return going_right


    #    [1,1,2,8]
    #    [48,24,6,1]
