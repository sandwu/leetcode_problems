
class Solution(object):
    """
    参照274的解法，取最优的二分法即可
    Runtime: 132 ms, faster than 45.22% of Python online submissions for H-Index II.
    Memory Usage: 16.5 MB, less than 57.46% of Python online submissions for H-Index II.
    """
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
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