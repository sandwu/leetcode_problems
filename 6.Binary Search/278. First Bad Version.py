
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

import bisect
class Solution(object):
    """
    用python 的库bisect来实现，指定0-n这样的list区间，然后对每个数进行isBadVersion(i)判断
    这里用到了__getitem__(self, i)的魔法方法，使得区间的每个数可以用索引访问，当为false时返回结果
    Runtime: 12 ms, faster than 93.14% of Python online submissions for First Bad Version.
    Memory Usage: 11.8 MB, less than 44.40% of Python online submissions for First Bad Version.
    """
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        class Wrap:
            def __getitem__(self, i):
                return isBadVersion(i)
        return bisect.bisect(Wrap(), False, 0, n)




class Solution2(object):
    """
    标准的二分法来解决，相当于是上面的解释版
    Runtime: 12 ms, faster than 93.14% of Python online submissions for First Bad Version.
    Memory Usage: 11.6 MB, less than 96.89% of Python online submissions for First Bad Version.
    """
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid -1):
                    return mid
                else:
                    end = mid
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:
                    start = mid + 1