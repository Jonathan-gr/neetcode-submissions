import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            pop1 = -1*heapq.heappop(stones)
            pop2 = -1*heapq.heappop(stones)
            new_stone = pop1-pop2
            if new_stone!=0:
                heapq.heappush(stones,-new_stone)

        return -stones[0] if len(stones)>0 else 0