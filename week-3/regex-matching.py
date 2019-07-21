class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows = len(s)
        cols = len(p)
        
        memo = [[False for x in range(cols+1)] for x in range(rows+1)]
        memo[0][0] = True
        
        # get regex for all optional patterns , a*b* etc
        for i in range(1, cols+1):
            if p[i-1] == '*':
                memo[0][i] = memo[0][i-2]
        
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    memo[i][j] = memo[i-1][j-1]
                    
                elif p[j-1] == '*':
                    memo[i][j] = memo[i][j-2]
                    
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        memo[i][j] = memo[i][j] | memo[i-1][j]
                
                else:
                    memo[i][j] = False
                    
        return memo[rows][cols]