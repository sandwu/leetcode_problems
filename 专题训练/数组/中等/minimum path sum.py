


class Solution:
    def minpathsum(self,grid):
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if row==col==0:
                    before = 0
                elif row == 0:
                    before = grid[row][col-1]
                elif col == 0:
                    before = grid[row-1][col]
                else:
                    before = min(grid[row][col-1],grid[row-1][col])
                grid[row][col] = before + grid[row][col]
        return grid[-1][-1]