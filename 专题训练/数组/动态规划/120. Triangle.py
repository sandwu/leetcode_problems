

"""
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

"""


class Solution(object): #递归，超时
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.triangle = triangle
        self.length = len(triangle)
        res = self.help(0, 0)
        return res

    def help(self, i, j):
        if i >= self.length: return 0
        left = self.help(i + 1, j) + self.triangle[i][j]
        right = self.help(i + 1, j + 1) + self.triangle[i][j]
        return min(left, right)

class Solution2(object): #备忘录，报错
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.triangle = triangle
        self.length = len(triangle)
        res = self.help(0, 0,{})
        return res

    def help(self, i, j, tmp):
        if i >= self.length: return 0
        key = str(i) + str(j)
        if tmp.get(key):return tmp[key]
        left = self.help(i + 1, j, tmp) + self.triangle[i][j]
        right = self.help(i + 1, j + 1, tmp) + self.triangle[i][j]
        val=min(left, right)
        tmp[key] = val
        return val


#DP[i,j] = min(DP[i+1, j], D[i+1, j+1]) + triangle[i,j]

class Solution3(object): #dp，自下向上
    """
    Runtime: 44 ms, faster than 75.34% of Python online submissions for Triangle.
    Memory Usage: 12.4 MB, less than 33.33% of Python online submissions for Triangle.
    """
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)-2,-1,-1):
            for j in range(i+1):
                triangle[i][j] = min(triangle[i+1][j],triangle[i+1][j+1]) + triangle[i][j]
        return triangle[0][0]
