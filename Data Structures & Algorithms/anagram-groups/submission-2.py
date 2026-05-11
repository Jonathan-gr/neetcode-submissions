class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        


        

        subLists = defaultdict(list)

        for word in strs:
            ordArr = [0]*26
            for w in word:
                ordArr[ord(w)-ord('a')]+=1

            subLists[tuple(ordArr)].append(word)
   
        return list(subLists.values())