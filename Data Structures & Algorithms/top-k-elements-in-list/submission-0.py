class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        arr = [ [] for _ in (range(len(nums)+1))]
        counter = Counter(nums)

        for key,val in counter.items():
            arr[val].append(key)
        
        res = []
        for i in reversed(range(len(nums)+1)):
            for val in arr[i]:
                res.append(val)
                k-=1
                if k<=0:
                    return res
        return res