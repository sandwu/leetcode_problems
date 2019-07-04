

class Solution(object):
    """
    题意是求得所有覆盖的面积，即两个长方形的和-公共部分，所以难点位于公共部分的求和
    公共部分通过分别求两个点的最大和最小值即可，详细看代码即可
    Runtime: 32 ms, faster than 97.54% of Python online submissions for Rectangle Area.
    Memory Usage: 11.6 MB, less than 86.06% of Python online submissions for Rectangle Area.
    """
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        overlap = max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0)
        return (A-C)*(B-D) + (E-G)*(F-H) - overlap