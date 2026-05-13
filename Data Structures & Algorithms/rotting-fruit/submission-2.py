
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = []
        fresh=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1
        if fresh ==0:
            return 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        res = -1
        while q:
            temp = []
            for i,j in q:
                for di,dj in directions:
                    ri,rj = di+i,dj+j

                    if ri<0 or rj<0 or ri>=len(grid) or rj>=len(grid[0]):
                        continue
                    
                    if grid[ri][rj] == 1:
                        grid[ri][rj]=2
                        temp.append([ri,rj])
                        fresh-=1
                
            res+=1
            q = temp
        return res if fresh==0 else -1
                    
                









