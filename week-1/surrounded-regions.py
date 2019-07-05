from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board:
            return
        
        q = deque([])
        rows, cols = len(board), len(board[0])
        
        if rows <= 2 or cols <= 2:
            return
        
        for row in range(rows):
            q.append((row, 0))
            q.append((row, cols-1))
            
        for col in range(cols):
            q.append((0, col))
            q.append((rows-1, col))
            
        while q:
            row, col = q.popleft()
            if 0 <= row < rows and 0 <= col < cols and board[row][col] == 'O':
                board[row][col] = "Pass"
                q.append((row-1, col))
                q.append((row+1, col))
                q.append((row, col-1))
                q.append((row, col+1))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "Pass":
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'