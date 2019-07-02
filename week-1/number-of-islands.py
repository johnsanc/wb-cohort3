class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rowLen, colLen = len(grid), len(grid[0]) 
        islands = 0
        
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == "1":
                    islands += 1
                    q = []
                    q.append([i, j])
                    
                    while q:
                        row, col = q.pop(0) # pop front of queue
                        if grid[row][col] == "1":
                            grid[row][col] = "0"
                            if row > 0 and grid[row - 1][col] == "1":
                                q.append([row - 1, col])
                            
                            if row < rowLen - 1 and grid[row + 1][col] == "1":
                                q.append([row + 1, col])
                            
                            if col > 0 and grid[row][col - 1] == "1":
                                q.append([row, col - 1])
                            
                            if col < colLen - 1 and grid[row][col + 1] == "1":
                                q.append([row, col + 1])
        return islands