



class Solution(object):
    """
    题意是给定二维数组1和0，分别代表陆地和水，求这二维数组中岛屿的数量，岛屿就是四周环绕水的陆地
    解法：bfs，根据当前的陆地去找寻环绕其周围的水
    Runtime: 108 ms, faster than 97.54% of Python online submissions for Number of Islands.
    Memory Usage: 19 MB, less than 50.00% of Python online submissions for Number of Islands.
    """
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def findIsland(grid, r, c):
            # to do
            if grid[r][c] == "1":
                grid[r][c] = "0"
            if r+ 1 < len(grid) and grid[r + 1][c] == "1":
                findIsland(grid, r + 1, c)
            if r - 1 >= 0 and grid[r - 1][c] == "1":
                findIsland(grid, r - 1, c)
            if c + 1 < len(grid[0]) and grid[r][c + 1] == "1":
                findIsland(grid, r, c + 1)
            if c - 1 >= 0 and grid[r][c - 1] == "1":
                findIsland(grid, r, c - 1)
            return 1

        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    res += findIsland(grid, row, col)

        return res