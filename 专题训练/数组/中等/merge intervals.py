

"""

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""











class Solution:
    def merge_intervals(self,intervals):
        res = []
        for i in sorted(intervals,key=lambda i:i[0]):
            if res and i[0] <= res[-1][-1]:
                res[-1][-1] = max(i[-1],res[-1][-1])
            else:
                res.append(i)
        return res