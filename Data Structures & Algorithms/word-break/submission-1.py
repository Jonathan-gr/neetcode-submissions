class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        


        dp = [False]*(len(s)+1)
        dp[-1]=True

        for i in reversed(range(len(s))):
            for word in wordDict:
                if i+len(word)<=len(s):
                    if word == s[i:i+len(word)]:
                        if not dp[i]:
                            dp[i]=dp[i+len(word)]
        
        return dp[0]