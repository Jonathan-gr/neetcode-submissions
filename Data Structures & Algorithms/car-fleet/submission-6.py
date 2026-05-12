class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
 

        position = sorted(list(zip(position,speed)),reverse=True)
        for i,(p,s) in enumerate(position):
            position[i] = ((target-p)/s)

        maxi = 0
        res=0
        for val in position:
            if val>maxi:
                maxi = val
                res+=1
        return res