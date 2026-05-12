class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        l,r = 0,len(heights)-1

        maxi=0
        while l<r:

            new_area = (r-l)*min(heights[l],heights[r])
            maxi = max(maxi,new_area)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxi