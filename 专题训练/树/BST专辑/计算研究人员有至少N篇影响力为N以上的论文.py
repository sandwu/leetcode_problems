
#274

class Solution(object):
    def hIndex2(self, citations):
        """直接遍历，每次取其后面的值和索引的差值与本身比较"""
        citations.sort()
        n = len(citations)
        h = 0
        for i,v in enumerate(citations):
            h = max(h, min(v,n-i))
        return h

    def hIndex(self, citations):
        """
        二分法加快遍历的速度
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        citations.sort()
        l, r = 0, N - 1
        H = 0
        while l <= r:
            mid = (r+l) >> 1
            H = max(H, min(citations[mid], N - mid)) #2
            if citations[mid] < N - mid:
                l = mid + 1
            else:
                r = mid - 1 #r = 1,l=0
        return H


citations = [3,0,6,1,5]
a = Solution()
a.hIndex(citations)