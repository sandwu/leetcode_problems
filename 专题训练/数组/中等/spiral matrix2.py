


class Solution:
    def spiralMatrix(self,n):
        x,u,d,l,r = 1,0,n-1,0,n-1
        res = [[0] * n for _ in range(n) ]
        while l < r and u < d:
            for i in range(l,r):
                res[u][i] = x
                x += 1
            for i in range(u,d):
                res[i][r] = x
                x += 1
            for i in range(r,l,-1):
                res[d][i] = x
                x += 1
            for i in range(d,u,-1):
                res[i][l] = x
                x += 1
            u,d,l,r = u+1,d-1,l+1,r-1
        if l==r:
            res[u][l] = x
        return res
