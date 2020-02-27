"""
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

"""

class Solution:
    def spiral_matrix(self,matrix):
        if not matrix or not matrix[0]:return []
        res = []
        m = len(matrix)
        n = len(matrix[0])
        u,d,l,r = 0,m-1,0,n-1
        while l<r and u < d:
            res.extend([matrix[u][i] for i in range(l,r)])
            res.extend([matrix[j][r] for j in range(u,d)])
            res.extend([matrix[d][i] for i in range(r,l,-1)])
            res.extend([matrix[j][l] for j in range(d,u,-1)])
            u,d,l,r = u+1,d-1,l+1,r-1

        if l==r:
            res.extend(matrix[i][l] for i in range(u,d+1))
        elif u==d:
            res.extend(matrix[u][j] for j in range(l, r + 1))
        return res