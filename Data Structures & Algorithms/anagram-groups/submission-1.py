class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        


        res = []

        subLists = defaultdict(list)

        for word in strs:
            temp = sorted(word)

            subLists[tuple(temp)].append(word)
   
        return list(subLists.values())