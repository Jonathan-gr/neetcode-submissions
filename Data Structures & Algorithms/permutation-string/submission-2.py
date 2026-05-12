class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        


        if len(s1)>len(s2):
            return False
        
        a1,a2 = [0]*26,[0]*26
        for i in range(len(s1)):
            a1[ord(s1[i])-ord('a')]+=1
            a2[ord(s2[i])-ord('a')]+=1
        


        def check_arrs(arr1,arr2):
            for i in range(26):
                if arr1[i]!=arr2[i]:
                    return False
            return True
        


        l=0
        for i in range(len(s1),len(s2)):
            if check_arrs(a1,a2):
                return True
            
            a2[ord(s2[l])-ord('a')]-=1
            a2[ord(s2[i])-ord('a')]+=1
            l+=1
        
        return check_arrs(a1,a2)
