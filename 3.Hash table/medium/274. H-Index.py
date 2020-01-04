

"""

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
"""


class Solution(object):
    """
    题意是求研究人员的n篇论文，一定有h篇大于h的引用，当满足多数的时候，就取最大的那个
    该解法先排序然后遍历，维护当前的一个最大引用h，因为已经排过序了，所以先取索引0的值与总共论文的数量最小值，
    假如索引0的值就高于总数量，则h一开始就是最大值总数量；如果不是，则慢慢取索引值和剩余论文的最小值，然后与维护的h值取最大
    Runtime: 24 ms, faster than 65.02% of Python online submissions for H-Index.
    Memory Usage: 11.9 MB, less than 47.22% of Python online submissions for H-Index.
    """
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        citations.sort()
        h = 0
        for i, c in enumerate(citations):
            h = max(h, min(N - i, c))
        return h

class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # 如果输入为空，返回0
        if not citations: return 0
        h = 0
        # 对输入的数据排序
        citations.sort()
        # 从后向前遍历
        for item in citations[-1::-1]:
            # 根据题意，至少有h个元素大于h
            h += 1
            # 如果出现当前元素小于h时，说明已经不满足给定的条件，函数返回
            if item < h:
                h -= 1
                break
        return h


class Solution3(object):
    """
    在第一种上进行了优化，避免了全部遍历，采用二分法来实现
    Runtime: 24 ms, faster than 76.49% of Python online submissions for H-Index.
    Memory Usage: 12 MB, less than 38.09% of Python online submissions for H-Index.
    """
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        citations.sort()
        l, r = 0, N - 1
        H = 0
        while l <= r:
            mid = l + (r - l) / 2
            H = max(H, min(citations[mid], N - mid))
            if citations[mid] < N - mid:
                l = mid + 1
            else:
                r = mid - 1
        return H