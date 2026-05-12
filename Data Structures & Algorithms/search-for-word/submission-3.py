class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def rec(i,j,length):
            if length == len(word):
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or (i,j) in seen or word[length]!=board[i][j]:
                return False
            

            seen.add((i,j))

            res = (
                rec(i+1,j,length+1) or
                rec(i-1,j,length+1) or
                rec(i,j+1,length+1) or
                rec(i,j-1,length+1)
            )

            seen.remove((i,j))
            return res



        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j]==word[0]:
                    seen = set()
                    if rec(i,j,0):
                        return True
        return False


