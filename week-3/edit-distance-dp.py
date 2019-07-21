class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        rows = len(word1)
        cols = len(word2)
        
        memo = [[0 for x in range(cols+1)] for x in range(rows+1)]

        for r in range(rows+1):
            for c in range(cols+1):

                if r == 0:
                    memo[r][c] = c

                elif c == 0:
                    memo[r][c] = r

                elif word1[r-1] == word2[c-1]:
                    memo[r][c] = memo[r-1][c-1]

                else:
                    memo[r][c] = min(memo[r-1][c],
                                     memo[r][c-1],
                                     memo[r-1][c-1]) + 1

        return memo[rows][cols]