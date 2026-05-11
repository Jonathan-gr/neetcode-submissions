class Solution:
    def climbStairs(self, n: int) -> int:
        

        if n<=3:
            return n
        one,two = 2,3

        for i in range(n-3):
            temp = one+two
            one = two
            two = temp

        return two