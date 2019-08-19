class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: 
            return False
        
        rows, cols = len(board), len(board[0])
        
        def dfs(row, col, board, word):
            if not word: return True # went through all letters
            
            # check bounds
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[0]:
                return False
            
            # Found the start
            start = board[row][col]
            
            # mark it so it can't be used
            board[row][col] = "*"
            
            # Recurse through all options
            answer = dfs(row-1, col, board, word[1:]) or dfs(row+1, col, board, word[1:]) or dfs(row, col-1, board, word[1:]) or dfs(row, col+1, board, word[1:])
            
            # Backtrack if not found
            board[row][col] = start
            
            return answer
            
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, board, word):
                    return True
        
        return False
            