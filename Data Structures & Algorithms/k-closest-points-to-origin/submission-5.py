import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        placements = defaultdict(list)
        heap_set = set()

        for x,y in points:

            distance =(x**2 + y**2)
            heap_set.add(distance)
            placements[distance].append([x,y])
        
        heap_set = list(heap_set)
        heapq.heapify(heap_set)
        
        res = []
        while k > 0:

            d = heapq.heappop(heap_set)

            for val in placements[d]:
                res.append(val)
                k-=1
        return res
        