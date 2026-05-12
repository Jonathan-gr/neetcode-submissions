class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        sety = set()

        l=0
        maxi=0
        for r in range(len(s)):
            
            while s[r] in sety:
                sety.remove(s[l])
                l+=1

            sety.add(s[r])
            maxi = max(maxi,(r-l+1))
        return maxi