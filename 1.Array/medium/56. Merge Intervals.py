
class Solution:
    """
    题目的要求是针对itervals里的所有集合做区间判断，如果有重叠的区间就合并，那就有以下几种情况：
    1.[1,3],[2,4]==>第二个的start小于第一个的end，第一个的end小于第二个的end
    2.[1,4],[2,3]==>第二个的start小于第一个的end，第二个的end小于第一个的end
    3.[2,4],[1,3]==>第二个的start大于第一个的start，通过排序解决该情况，则转换为第1、2种
    4.[1,2],[3,4]==>即没有重叠空间
    所以如果排完序后，就剩1，2两种情况，本质是比较第一个和第二个的end，转为代码如下
    Runtime: 60 ms, faster than 80.12% of Python3 online submissions for Merge Intervals.
    Memory Usage: 15.9 MB, less than 5.34% of Python3 online submissions for Merge Intervals.
    """
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        out = []
        for i in sorted(intervals, key=lambda i:i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(i.end, out[-1].end)
            else:
                out.append(i)
        return out