class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count = 4
                    if r-1 >= 0:
                        if grid[r-1][c] == 1: count -= 1 # top
                    if r+1 < rows:
                        if grid[r+1][c] == 1: count -= 1 # bottom
                    if c-1 >= 0:
                        if grid[r][c-1] == 1: count -= 1 # left
                    if c+1 < cols:
                        if grid[r][c+1] == 1: count -= 1 # right
                    perimeter += count
                    print(count)
                        
        return perimeter
                    