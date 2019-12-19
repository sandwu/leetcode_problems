


#题意是给定n和对应的函数判别错误版本，需要求1-n之间的第一个错误版本，用二分法来搞

def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        start = 1
        end = n
        while start <= end:
            mid = (start + end) >> 1
            if isBadVersion(mid):
                if isBadVersion(mid-1):
                    end = mid-1
                else:
                    return mid
            else:
                if isBadVersion(mid+1):
                    return mid+1
                else:
                    start = mid+1
