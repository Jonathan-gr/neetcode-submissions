class Solution:
    def trap(self, height: List[int]) -> int:
        


        l,r = 0,len(height)-1

        max_left,max_right = 0,0
        res=0

        while l<r:

            max_left = max(max_left,height[l])
            max_right = max(max_right,height[r])


            if max_left>height[l] and height[l]<max_right:
                res+=min(max_left,max_right)-height[l]
            
            elif max_left>height[r] and height[r]<max_right:
                res+=min(max_left,max_right)-height[r]
            

            if max_left<max_right:
                l+=1
            else:
                r-=1
        return res