class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

        gas = [gas[i]-cost[i] for i in range(len(gas))]
        if sum(gas)<0:
            return -1



        res=0
        curr = 0
        for i in (range(len(gas))):
            curr+=gas[i]
            if curr<0:
                curr=0
                res=i+1
                
        return res