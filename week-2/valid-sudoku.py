class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        is_valid = True
        
        # check rows
        for r in range(9):
            row_set = set()
            for c in range(9):
                if board[r][c] not in row_set and board[r][c].isnumeric():
                    row_set.add(board[r][c])
                elif board[r][c] in row_set:
                    return False
        
        # check columns
        for c in range(9):
            col_set = set()
            for r in range(9):
                if board[r][c] not in col_set and board[r][c].isnumeric():
                    col_set.add(board[r][c])
                elif board[r][c] in col_set:
                    return False
        
        # check 3x3
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                square = set()
                if board[r][c] not in square and board[r][c].isnumeric():
                    square.add(board[r][c])
                elif board[r][c] in square:
                    return False
                
                if board[r][c+1] not in square and board[r][c+1].isnumeric():
                    square.add(board[r][c+1])
                elif board[r][c+1] in square:
                    return False
                
                if board[r][c+2] not in square and board[r][c+2].isnumeric():
                    square.add(board[r][c+2])  
                elif board[r][c+2] in square:
                    return False
                
                if board[r+1][c] not in square and board[r+1][c].isnumeric():
                    square.add(board[r+1][c])
                elif board[r+1][c] in square:
                    return False
                
                if board[r+1][c+1] not in square and board[r+1][c+1].isnumeric():
                    square.add(board[r+1][c+1]) 
                elif board[r+1][c+1] in square:
                    return False
                
                if board[r+1][c+2] not in square and board[r+1][c+2].isnumeric():
                    square.add(board[r+1][c+2])
                elif board[r+1][c+2] in square: 
                    return False
                
                if board[r+2][c] not in square and board[r+2][c].isnumeric():
                    square.add(board[r+2][c])  
                elif board[r+2][c] in square: 
                    return False
                
                if board[r+2][c+1] not in square and board[r+2][c+1].isnumeric(): 
                    square.add(board[r+2][c+1])  
                elif board[r+2][c+1] in square: 
                    return False
                
                if board[r+2][c+2] not in square and board[r+2][c+2].isnumeric():
                    square.add(board[r+2][c+2])  
                elif board[r+2][c+2] in square:
                    return False
        return is_valid