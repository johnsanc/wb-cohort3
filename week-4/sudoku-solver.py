class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def solve_part(i, j):
            l = len(board)
            if i == l:
                i = 0
                j += 1
                if j == len(board[i]):
                    return True
            if board[i][j] != '.': # empty
                return solve_part(i + 1, j)
                
            def valid_add(i, j, value):
                if any(str(value) == board[k][j] for k in range(l)):
                    return False

                if str(value) in board[i]:
                    return False

                region = int(math.sqrt(l))
                I = i // region
                J = j // region
                return not any(
                    str(val) == board[region * I + a][region * J + b] 
                    for a,b in itertools.product(range(region), repeat=2))
        
            for val in range(1, l + 1):
                if valid_add(i, j, val):
                    board[i][j] = str(val)
                    if solve_part(i + 1, j):
                        return True
            