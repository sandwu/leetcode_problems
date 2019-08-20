



class Solution:
    """
    题意是求一个方形矩阵中，1假设为陆地，0假设为水，最远距离的陆地和水是多远，默认左上角为(0.0)
    解法通过BFS，即先找出1的点，然后在1的上下左右找到0的点为一层，把该点设为1，再围绕这个1去找对应的
    外面一层0的店，直到找完全部
    """
    def maxDistance(self, grid: List[List[int]]) -> int:
        from collections import deque
        m,n = len(grid), len(grid[0])
        q = deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        if len(q) == m * n or len(q) == 0: return -1
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i,j = q.popleft()
                for x,y in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    xi, yj = x+i, y+j
                    if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
                        q.append((xi, yj))
                        grid[xi][yj] = 1
            level += 1
        return level-1